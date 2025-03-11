import unittest
from tasks import task


class MyTestCase(unittest.TestCase):
    def test_empty_string(self):
        # Given
        value = ""
        exp_value = 0
        # When
        result = task(value)
        # Then
        self.assertEqual(result, exp_value)

    def test_return_value(self):
        # Given
        value = "2"
        exp_value = 2
        # When
        result = task(value)
        # Then
        self.assertEqual(result, exp_value)

    def test_2comma_sum(self):
        # Given
        value = "2,2"
        exp_value = 4
        # When
        result = task(value)
        # Then
        self.assertEqual(result, exp_value)

    def test_2newline_sum(self):
        # Given
        value = "2\n2"
        exp_value = 4
        # When
        result = task(value)
        # Then
        self.assertEqual(result, exp_value)

    def test_3anycomma_sum(self):
        # Given
        value = "2,2,2"
        exp_value = 6
        # When
        result = task(value)
        # Then
        self.assertEqual(result, exp_value)

    def test_3anynewline_sum(self):
        # Given
        value = "2\n2\n2"
        exp_value = 6
        # When
        result = task(value)
        # Then
        self.assertEqual(result, exp_value)

    def test_negative_number(self):
        # Given
        value = "-10,-5,2"
        error_message = "No negative numbers!"
        # When / Then
        with self.assertRaises(ValueError) as context:
            task(value)
        self.assertIn(error_message, str(context.exception))

    def test_greaterthan1000_number(self):
        # Given
        value = "1001,5,2"
        exp_value = 7
        # When
        result = task(value)
        # Then
        self.assertEqual(result, exp_value)

    def test_1custom_delimiter(self):
        # Given
        value = "//#\n2#2"
        exp_value = 4
        # When
        result = task(value)
        # Then
        self.assertEqual(result, exp_value)

    def test_2custom_delimiter(self):
        # Given
        value = "//[##]\n2##2"
        exp_value = 4
        # When
        result = task(value)
        # Then
        self.assertEqual(result, exp_value)

    def test_manybig_delimiters(self):
        # Given
        value = "//[##][%%%]\n2##2%%%2"
        exp_value = 6
        # When
        result = task(value)
        # Then
        self.assertEqual(result, exp_value)

    def test_manymixed_delimiters(self):
        # Given
        value = "//[##][%%%]\n2##2%%%2"
        exp_value = 6
        # When
        result = task(value)
        # Then
        self.assertEqual(result, exp_value)

if __name__ == '__main__':
    unittest.main()
