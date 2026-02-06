import unittest # a testing framework
from quiz_data import load_questions # converts to dict
from quiz_utils import clean_name # cleans the name


class TestSmoke(unittest.TestCase):

    def test_load_questions_runs(self):
        self.assertTrue(1)

class TestQuizData(unittest.TestCase):

    def test_load_questions_runs(self):
        questions = load_questions()
        self.assertIsNotNone(questions)
        
    def test_clean_name(self):
        self.assertEqual(clean_name("  john doe  "), "John Doe")
        self.assertEqual(clean_name("BOB JOHNSON"), "Bob Johnson")

if __name__ == "__main__":
    unittest.main()
