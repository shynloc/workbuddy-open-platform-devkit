import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
import check_bilingual_docs as checker


class BilingualDocsTests(unittest.TestCase):
    def report(self, zh, en, *flags):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            registry = root/'pairs.json'
            registry.write_text(json.dumps({'pairs': [{
                'id': 'skill', 'zh': 'https://example.test/zh',
                'en': 'https://example.test/en',
                'required_literals': ['name', 'user-invocable', 'allowed-tools'],
            }]}), 'utf-8')
            args = ['check', '--registry', str(registry), '--json-out', str(root/'report.json'),
                    '--markdown-out', str(root/'report.md'), *flags]
            results = [zh, en]
            with patch.object(sys, 'argv', args), patch.object(checker, 'fetch', side_effect=results), \
                    contextlib.redirect_stdout(io.StringIO()):
                status = checker.main()
            return status, json.loads((root/'report.json').read_text('utf-8'))['pairs'][0], \
                (root/'report.md').read_text('utf-8')

    def test_matching_literals_pass(self):
        text = 'name user-invocable allowed-tools'
        status, row, _ = self.report((200, text), (200, text), '--fail-on-mismatch')
        self.assertEqual(status, 0)
        self.assertTrue(row['ok'])
        self.assertFalse(row['review_required'])

    def test_shared_absence_requires_review_without_translation_mismatch(self):
        status, row, md = self.report((200, 'name allowed-tools'), (200, 'name allowed-tools'),
                                      '--fail-on-mismatch')
        self.assertEqual(status, 0)
        self.assertFalse(row['mismatch'])
        self.assertTrue(row['review_required'])
        self.assertEqual(row['missing_in_both'], ['user-invocable'])
        self.assertEqual(row['missing_in_zh'], [])
        self.assertEqual(row['missing_in_en'], [])
        self.assertIn('user-invocable', md)
        self.assertIn('REVIEW', md)

    def test_optional_shared_absence_gate(self):
        status, _, _ = self.report((200, 'name allowed-tools'), (200, 'name allowed-tools'),
                                   '--fail-on-shared-missing')
        self.assertEqual(status, 2)

    def test_one_sided_absence_in_either_direction_fails(self):
        for reverse in (False, True):
            values = [(200, 'name allowed-tools'), (200, 'name user-invocable allowed-tools')]
            if reverse:
                values.reverse()
            with self.subTest(reverse=reverse):
                status, row, _ = self.report(*values, '--fail-on-mismatch')
                self.assertEqual(status, 2)
                self.assertTrue(row['mismatch'])
                self.assertEqual(row['missing_in_en' if reverse else 'missing_in_zh'], ['user-invocable'])

    def test_common_absence_does_not_hide_one_sided_absence(self):
        status, row, _ = self.report((200, 'name'), (200, 'name allowed-tools'), '--fail-on-mismatch')
        self.assertEqual(status, 2)
        self.assertEqual(row['missing_in_both'], ['user-invocable'])
        self.assertEqual(row['missing_in_zh'], ['allowed-tools'])

    def test_fetch_failure_and_http_error_fail(self):
        for response in (OSError('offline'), (500, 'name user-invocable allowed-tools')):
            with self.subTest(response=str(response)):
                status, row, _ = self.report(response, (200, 'name user-invocable allowed-tools'),
                                              '--fail-on-mismatch')
                self.assertEqual(status, 2)
                self.assertFalse(row['ok'])

    def test_size_warning_is_review_signal(self):
        text = 'name user-invocable allowed-tools'
        status, row, _ = self.report((200, text), (200, text+' more'*100), '--fail-on-mismatch')
        self.assertEqual(status, 0)
        self.assertTrue(row['size_warning'])
        self.assertTrue(row['review_required'])

    def test_literals_match_identifiers_not_substrings(self):
        self.assertFalse(checker.contains('display_name display_name_en', 'name'))
        self.assertFalse(checker.contains('description_zh', 'description'))
        self.assertTrue(checker.contains('`NAME`: skill', 'name'))
        self.assertTrue(checker.contains('POST /openapi/v2/token', '/openapi/v2/token'))

    def test_chinese_neighbors_and_longer_ascii_identifiers(self):
        for text in ('需要user-invocable字段','需要user-invocable','user-invocable字段'):
            with self.subTest(text=text):
                self.assertTrue(checker.contains(text,'user-invocable'))
        for text in ('preuser-invocablepost','pre-user-invocable','user-invocable-extra','user-invocable_extra'):
            self.assertFalse(checker.contains(text,'user-invocable'))
        status,row,_ = self.report((200,'name allowed-tools 需要user-invocable字段'),
                                   (200,'name allowed-tools'),'--fail-on-mismatch')
        self.assertEqual(status,2)
        self.assertEqual(row['missing_in_en'],['user-invocable'])
        self.assertEqual(row['missing_in_both'],[])
        status,row,_ = self.report((200,'name allowed-tools 需要user-invocable字段'),
                                   (200,'name allowed-tools user-invocable'),'--fail-on-mismatch')
        self.assertEqual(status,0)
        self.assertFalse(row['mismatch'])


if __name__ == '__main__':
    unittest.main()
