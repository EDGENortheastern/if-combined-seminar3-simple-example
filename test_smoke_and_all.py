import unittest # a testing framework
from quiz_data import load_questions # converts to dict
from quiz_utils import clean_name # cleans the name
from quiz_utils import character_check # validates the name


class TestSmoke(unittest.TestCase):

    def test_load_questions_runs(self):
        self.assertTrue(1)

class TestQuiz(unittest.TestCase):

    def test_load_questions_runs(self):
        questions = load_questions()
        self.assertIsNotNone(questions)
        
    def test_clean_name(self):
        self.assertEqual(clean_name("  john doe  "), "John Doe")
        self.assertEqual(clean_name("BOB JOHNSON"), "Bob Johnson")
        
    def test_character_check_happy(self):
        self.assertTrue(character_check("Alice"))
        self.assertTrue(character_check("Alice Smith"))

    def test_character_check_unhappy(self):
        self.assertFalse(character_check("Alice1"))
        self.assertFalse(character_check("123"))

if __name__ == "__main__":
    unittest.main()
