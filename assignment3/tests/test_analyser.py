import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analytics.analyser import SleepAnalyser

class TestAnalyser(unittest.TestCase):
    def setUp(self):
        self.sample = [
            {'sleep_hours': '5', 'gpa': '3.0'},
            {'sleep_hours': '8', 'gpa': '4.0'}
        ]
        self.analyser = SleepAnalyser(self.sample)

    def test_total_students(self):
        self.assertEqual(len(self.analyser.students), 2)

    def test_result_is_not_empty(self):
        res = self.analyser.analyse()
        self.assertTrue(len(res) > 0)

    def test_result_has_required_keys(self):
        res = self.analyser.analyse()
        self.assertIn('low_sleep', res)
        self.assertIn('gpa_difference', res)

    def test_analyse_twice(self):
        res1 = self.analyser.analyse()
        res2 = self.analyser.analyse()
        self.assertEqual(res1, res2)

if __name__ == '__main__':
    unittest.main()