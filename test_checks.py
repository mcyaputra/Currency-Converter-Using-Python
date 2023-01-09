import unittest
from checks import check_arguments, check_date

class TestCheckArguments(unittest.TestCase):
    """
    Testing check_arguments() function in checks.py
    """
    def test_check_three_arguments(self):
        data = ['2020-01-01', 'USD', 'AUD']
        result = check_arguments(data)
        self.assertEqual(result, data)

class TestCheckDate(unittest.TestCase):
    """
    Testing check_date() function in checks.py
    """
    def test_check_date(self):
        data = '2022-01-01'
        result = check_date(data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()