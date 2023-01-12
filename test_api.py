import unittest
from api import call_get

class TestAPI(unittest.TestCase):
    """
    Testing call_get() function in api.py
    """
    def test_api_url(self):
        test_api = call_get("https://api.frankfurter.app")
        test_status_code = 200
        self.assertEqual(test_api.status_code, test_status_code)

if __name__ == '__main__':
    unittest.main()

