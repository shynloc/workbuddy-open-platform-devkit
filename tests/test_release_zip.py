import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
from smoke_test_templates import write_png
from validate_release_zip import validate_archive


class ReleaseZipTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name)
        self.skill = self.base/'demo-skill'
        result = self.command('scaffold.py', 'skill', 'demo-skill', self.skill)
        self.assertEqual(result.returncode, 0, result.stdout+result.stderr)

    def command(self, script, *args):
        return subprocess.run([sys.executable, str(ROOT/'scripts'/script), *map(str, args)],
                              text=True, capture_output=True, encoding='utf-8')

    def archive(self, root, name='test.zip', transform=lambda name: name, omit=lambda name: False):
        out = self.base/name
        with zipfile.ZipFile(out, 'w') as z:
            for file in root.rglob('*'):
                if file.is_file():
                    relative = file.relative_to(root).as_posix()
                    if not omit(relative):
                        z.write(file, transform(root.name+'/'+relative))
        return out

    def expert(self):
        root = self.base/'expert'
        shutil.copytree(ROOT/'90-templates/expert-template', root)
        write_png(root/'avatars/expert.png')
        embedded = root/'skills/embedded'
        embedded.mkdir(parents=True)
        (embedded/'SKILL.md').write_text('---\nname: embedded\ndescription: Internal task\n---\n# Internal\n','utf-8')
        config = root/'.codebuddy-plugin/plugin.json'
        data = json.loads(config.read_text('utf-8'))
        data['skills'] = ['./skills/embedded']
        config.write_text(json.dumps(data,ensure_ascii=False),'utf-8')
        (root/'.mcp.json').write_text('{"mcpServers": {}}','utf-8')
        return root

    def test_generated_archive_and_flat_logical_root(self):
        out = self.base/'skill.zip'
        result = self.command('pack_release.py', self.skill, '--out', out)
        self.assertEqual(result.returncode, 0, result.stdout+result.stderr)
        validate_archive(out, 'skill', self.skill)
        with zipfile.ZipFile(out) as z:
            self.assertIsNone(z.testzip())
            self.assertIn('demo-skill/SKILL.md', z.namelist())
        flat = self.archive(self.skill, 'flat.zip', lambda n:n.split('/',1)[1])
        validate_archive(flat, 'skill', self.skill)

    def test_wrong_entry_missing_file_case_and_extra_wrapper(self):
        variants = [
            ('nested.zip', lambda n:'outer/'+n, lambda n:False),
            ('missing.zip', lambda n:n, lambda n:n=='SKILL.md'),
            ('case.zip', lambda n:n.replace('SKILL.md','skill.md'), lambda n:False),
        ]
        for name, transform, omit in variants:
            with self.subTest(name=name), self.assertRaises(ValueError):
                validate_archive(self.archive(self.skill,name,transform,omit), 'skill')
        with self.assertRaises(ValueError):
            validate_archive(self.archive(self.skill), 'expert')

    def test_actual_zip_content_must_match_source(self):
        out = self.archive(self.skill)
        (self.skill/'SKILL.md').write_text((self.skill/'SKILL.md').read_text('utf-8')+'\nChanged body\n','utf-8')
        with self.assertRaisesRegex(ValueError, 'differs'):
            validate_archive(out, 'skill', self.skill)

    def test_multiple_asset_markers_are_rejected(self):
        expert = self.expert()
        for root,marker,typ in [(self.skill,'connector-meta.json','skill'),
                                 (expert,'SKILL.md','expert'),
                                 (expert,'connector-meta.json','connector')]:
            path = root/marker
            path.write_text('{}','utf-8')
            try:
                with self.subTest(marker=marker,typ=typ), self.assertRaisesRegex(ValueError,'ambiguous'):
                    validate_archive(self.archive(root),'%s' % typ)
            finally:
                path.unlink()

    def test_hidden_plugin_manifest_and_embedded_skill(self):
        root = self.expert()
        out = self.base/'expert.zip'
        result = self.command('pack_release.py',root,'--out',out)
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        validate_archive(out,'expert',root)
        with zipfile.ZipFile(out) as z:
            self.assertIn('expert/.codebuddy-plugin/plugin.json',z.namelist())
            self.assertIn('expert/.mcp.json',z.namelist())
            self.assertIn('expert/skills/embedded/SKILL.md',z.namelist())
        with self.assertRaises(ValueError):
            validate_archive(self.archive(root,'no-hidden.zip',omit=lambda n:n.startswith('.')), 'expert')
        (root/'skills/embedded/SKILL.md').unlink()
        with self.assertRaisesRegex(ValueError,'missing'):
            validate_archive(self.archive(root,'missing-embedded.zip'),'expert')

    def test_plugin_field_types_and_declared_paths(self):
        root = self.expert()
        config = root/'.codebuddy-plugin/plugin.json'
        original = json.loads(config.read_text('utf-8'))
        for key,value in [('skills','./skills/embedded'),('author','Author'),('keywords','word'),
                          ('skills',['../outside']),('agents',['./agents/YOUR-EXPERT.md'])]:
            data = dict(original, **{key:value})
            config.write_text(json.dumps(data),'utf-8')
            with self.subTest(key=key,value=value), self.assertRaises(ValueError):
                validate_archive(self.archive(root), 'expert')

    def test_embedded_skill_and_team_settings_case_is_exact(self):
        expert = self.expert()
        out = self.archive(expert,'embedded-case.zip',lambda n:n.replace('/embedded/SKILL.md','/embedded/skill.md'))
        with self.assertRaises(ValueError):
            validate_archive(out,'expert')
        team = self.base/'team'
        shutil.copytree(ROOT/'90-templates/expert-team-template',team)
        for name in ('team.png','team-lead.png','research-specialist.png','delivery-specialist.png'):
            write_png(team/'avatars'/name)
        out = self.archive(team,'team.zip')
        validate_archive(out,'expert-team',team)
        out = self.archive(team,'settings-case.zip',lambda n:n.replace('/settings.json','/Settings.json'))
        with self.assertRaises(ValueError):
            validate_archive(out,'expert-team')

    def test_windows_normalization_cannot_shadow_skill_metadata(self):
        complete = (self.skill/'SKILL.md').read_bytes()
        (self.skill/'SKILL.md').write_text(complete.decode('utf-8').replace('name: demo-skill\n',''),'utf-8')
        for suffix in ('.',' '):
            out = self.archive(self.skill)
            with zipfile.ZipFile(out,'a') as z:
                z.writestr('demo-skill/SKILL.md'+suffix,complete)
            with self.subTest(suffix=suffix), self.assertRaises(ValueError):
                validate_archive(out,'skill')

    def test_declared_nested_agents_and_mcp_files_are_checked(self):
        root = self.expert()
        config = root/'.codebuddy-plugin/plugin.json'
        original = json.loads(config.read_text('utf-8'))
        data = dict(original,dependencies={'mcpServers':'./missing.mcp.json'})
        config.write_text(json.dumps(data),'utf-8')
        with self.assertRaisesRegex(ValueError,'missing declared path'):
            validate_archive(self.archive(root),'expert')
        data = dict(original)
        nested = root/'agents/nested/your-expert.md'
        nested.parent.mkdir()
        nested.write_text('# No frontmatter\n','utf-8')
        data['agents'] = ['./agents/nested/your-expert.md']
        config.write_text(json.dumps(data),'utf-8')
        with self.assertRaises(ValueError):
            validate_archive(self.archive(root),'expert')
        shutil.copyfile(root/'agents/your-expert.md',nested)
        validate_archive(self.archive(root),'expert',root)

    def test_unsafe_duplicate_and_temporary_entries(self):
        for extra in ('../escape.txt','demo-skill/.env','demo-skill/skill.md','demo-skill//SKILL.md'):
            out = self.archive(self.skill)
            with zipfile.ZipFile(out,'a') as z:
                z.writestr(extra,'bad')
            with self.subTest(extra=extra), self.assertRaises(ValueError):
                validate_archive(out,'skill')
        self.assertFalse((self.base/'escape.txt').exists())

    def test_packer_rejects_invalid_input_and_output_inside_source(self):
        for source,out in [(self.base/'absent',self.base/'absent.zip'),
                           (self.skill,self.skill/'self.zip')]:
            result = self.command('pack_release.py',source,'--out',out)
            self.assertNotEqual(result.returncode,0,result.stdout)
            self.assertFalse(out.exists())

    def test_yaml_comment_metadata_and_release_artifact_agree(self):
        skill = self.skill/'SKILL.md'
        text = skill.read_text('utf-8').replace('name: demo-skill','name: demo-skill # identifier')
        skill.write_text(text.replace('version: 1.0.0','version: 1.0.0 # release note'),'utf-8')
        dist = self.base/'release'
        result = self.command('release_check.py',self.skill,'--dist',dist,'--side-effect-review','not-applicable')
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        manifest = json.loads((dist/'demo-skill-v1.0.0.manifest.json').read_text('utf-8'))
        self.assertEqual(manifest['asset']['name'],'demo-skill')
        self.assertEqual(manifest['asset']['version'],'1.0.0')
        self.assertIn('Version: 1.0.0',(dist/'demo-skill-v1.0.0.submission-notes.md').read_text('utf-8'))
        validate_archive(dist/'demo-skill-v1.0.0.zip','skill',self.skill)
        direct = self.base/'direct.json'
        result = self.command('generate_release_manifest.py',self.skill,'--output',direct)
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        self.assertEqual(json.loads(direct.read_text('utf-8'))['asset']['version'],'1.0.0')


if __name__ == '__main__':
    unittest.main()
