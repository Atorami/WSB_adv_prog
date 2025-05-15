import unittest
from awesome_lib.data_utils import is_valid_email, convert_date_format

class TestDataUtils(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(is_valid_email("test@test.com"))

    def test_invalid_email(self):
        self.assertFalse(is_valid_email("test@.com"))

    def test_date_conversion(self):
        self.assertEqual(convert_date_format("31-12-2023"), "2023-12-31")

    def test_date_conversion_invalid(self):
        with self.assertRaises(ValueError):
            convert_date_format("31/05/2017")
