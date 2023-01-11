import unittest
from frankfurter import Frankfurter

class TestUrl(unittest.TestCase):
    """
    Testing the url attributes of Frankfurter class in checks.py
    """ 
    def setUp(self) -> None:
        self.Furter = Frankfurter()
        self.base_url = 'https://api.frankfurter.app'
        self.currencies_url = 'https://api.frankfurter.app/currencies'
        self.historical_url = 'https://api.frankfurter.app/latest?to=USD,GBP'
        self.currencies = []
    
    def test_url(self):
        self.assertEqual(self.Furter.base_url, self.base_url)
        self.assertEqual(self.Furter.currencies_url, self.currencies_url)
        self.assertEqual(self.Furter.historical_url, self.historical_url)


class TestCurrenciesList(unittest.TestCase):
    """
    Testing currencies attributes of the Frankfurter class in frankfurter.py
    """
    def setUp(self) -> None:
        self.Furter = Frankfurter()

    def test_currencies_list(self):
        target_currency = 'USD'
        result = self.Furter.get_currencies_list()
        self.assertIn(target_currency, result)


class TestCheckCurrency(unittest.TestCase):
    """
    Testing the Frankfurter class' check_currency() method in frankfurter.py
    """
    def setUp(self) -> None:
        self.Furter = Frankfurter()

    def test_check_currency(self):
        target_currency = 'USD'
        result = self.Furter.check_currency(target_currency)
        self.assertTrue(result)


class TestHistoricalRate(unittest.TestCase):
    """
    Testing the Frankfurter class' get_historical_rate() method in frankfurter.py
    """
    def setUp(self) -> None:
        self.Furter = Frankfurter()
    
    def test_historical_rate(self):
        target = 1.3908
        self.from_currency = 'USD'
        self.to_currency = 'AUD'
        self.from_date = '2020-10-10'
        result = self.Furter.get_historical_rate(self.from_currency, self.to_currency, self.from_date, amount=1).get('rates').get(self.to_currency)
        self.assertEqual(target, result)

if __name__ == '__main__':
    unittest.main()