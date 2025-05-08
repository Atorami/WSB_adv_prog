import unittest
from app import is_valid_email, calculate_rectangle_area, filter_even_numbers, convert_date_format, is_palindrome

class TestAppFunctions(unittest.TestCase):

    def setUp(self):
        # Przykładowe dane do testów
        self.valid_email = "test@test.com"
        self.invalid_email = "invalid-email.com"
        self.rectangle_sides = (5, 10)
        self.numbers_list = [1, 2, 3, 4, 5, 6]
        self.date_input = "08-05-2025"
        self.palindrome_text = "Zakopane na pokaz"
        self.non_palindrome_text = "To nie jest palindrom"

    # Testy dla is_valid_email
    def test_valid_email(self):
        self.assertTrue(is_valid_email(self.valid_email))

    def test_invalid_email(self):
        self.assertFalse(is_valid_email(self.invalid_email))

    def test_empty_email(self):
        self.assertFalse(is_valid_email(""))

    # Testy dla calculate_rectangle_area
    def test_area_calculation(self):
        self.assertEqual(calculate_rectangle_area(5, 10), 50)

    def test_area_with_zero(self):
        self.assertEqual(calculate_rectangle_area(0, 10), 0)

    def test_area_with_negative(self):
        with self.assertRaises(ValueError):
            calculate_rectangle_area(-5, 10)

    # Testy dla filter_even_numbers
    def test_filter_even_numbers(self):
        self.assertEqual(filter_even_numbers(self.numbers_list), [2, 4, 6])

    def test_filter_even_numbers_empty(self):
        self.assertEqual(filter_even_numbers([]), [])

    def test_filter_even_numbers_all_odd(self):
        self.assertEqual(filter_even_numbers([1, 3, 5]), [])

    # Testy dla convert_date_format
    def test_convert_date_format_correct(self):
        self.assertEqual(convert_date_format(self.date_input), "2025/05/08")

    def test_convert_date_format_invalid(self):
        with self.assertRaises(ValueError):
            convert_date_format("2025-05-08")

    def test_convert_date_format_empty(self):
        with self.assertRaises(ValueError):
            convert_date_format("")

    # Testy dla is_palindrome
    def test_is_palindrome_true(self):
        self.assertTrue(is_palindrome(self.palindrome_text))

    def test_is_palindrome_false(self):
        self.assertFalse(is_palindrome(self.non_palindrome_text))

    def test_is_palindrome_empty(self):
        self.assertTrue(is_palindrome(""))


if __name__ == '__main__':
    unittest.main()
