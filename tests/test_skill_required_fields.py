"""Required fields must fail in both public validation entry points."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ('name', 'display_name', 'display_name_en', 'description',
            'description_zh', 'description_en', 'version', 'author')


class SkillRequiredFieldsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = Draft202012Validator(json.loads(
            (ROOT/'schemas/skill-frontmatter.schema.json').read_text('utf-8')))
        text = (ROOT/'90-templates/skill-template/SKILL.md').read_text('utf-8')
        cls.valid = yaml.safe_load(text.split('---', 2)[1])

    def run_validator(self, frontmatter, script='validate_skill.py'):
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, 'SKILL.md').write_text(
                '---\n'+yaml.safe_dump(frontmatter, allow_unicode=True)+'---\n# Test\n', 'utf-8')
            return subprocess.run([sys.executable, str(ROOT/'scripts'/script), tmp],
                                  text=True, capture_output=True, encoding='utf-8')

    def test_complete_starter_passes_both_validators(self):
        self.assertTrue(self.schema.is_valid(self.valid))
        for script in ('validate_skill.py', 'validate_asset_schemas.py'):
            with self.subTest(script=script):
                result = self.run_validator(self.valid, script)
                self.assertEqual(result.returncode, 0, result.stdout+result.stderr)

    def test_each_required_field_missing_fails_both_validators(self):
        for field in REQUIRED:
            value = dict(self.valid)
            del value[field]
            with self.subTest(field=field):
                self.assertFalse(self.schema.is_valid(value), field)
                for script in ('validate_skill.py', 'validate_asset_schemas.py'):
                    result = self.run_validator(value, script)
                    self.assertEqual(result.returncode, 1, result.stdout+result.stderr)
                    self.assertIn(field, result.stdout)

    def test_empty_or_null_required_fields_fail(self):
        for field in REQUIRED:
            for empty in ('', None):
                with self.subTest(field=field, value=empty):
                    value = dict(self.valid, **{field: empty})
                    self.assertFalse(self.schema.is_valid(value))
                    result = self.run_validator(value)
                    self.assertEqual(result.returncode, 1, result.stdout+result.stderr)
                    self.assertIn(field, result.stdout)

    def test_existing_skill_packages_have_required_fields(self):
        for parent in ('90-templates', 'examples'):
            for path in (ROOT/parent).rglob('SKILL.md'):
                with self.subTest(path=str(path.relative_to(ROOT))):
                    fields = yaml.safe_load(path.read_text('utf-8').split('---', 2)[1])
                    self.assertTrue(self.schema.is_valid(fields), str(path))

    def test_non_string_required_values_fail_without_traceback(self):
        for value in (False, 123, ['name'], {'name': 'nested'}):
            with self.subTest(value=value):
                fields = dict(self.valid, name=value)
                self.assertFalse(self.schema.is_valid(fields))
                result = self.run_validator(fields)
                self.assertEqual(result.returncode, 1)
                self.assertIn('name', result.stdout)
                self.assertNotIn('Traceback', result.stderr)

    def test_legacy_invocation_fields_remain_accepted(self):
        for value in (False, True):
            fields = dict(self.valid, **{'user-invocable': value, 'disable-model-invocation': value})
            self.assertTrue(self.schema.is_valid(fields))
            self.assertEqual(self.run_validator(fields).returncode, 0)


if __name__ == '__main__':
    unittest.main()
