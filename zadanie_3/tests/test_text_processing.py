import unittest
from awesome_lib.text_processing import is_palindrome, clean_text, count_words

class TestTextProcessing(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("Kajak"))

    def test_clean_text(self):
        self.assertEqual(clean_text("abc123!?"), "abc")

    def test_count_words(self):
        self.assertEqual(count_words("Some test text"), 3)