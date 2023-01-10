import unittest
from currency import CurrencyConverter

class TestCurrencyConverterInstantiation(unittest.TestCase):
    """
    Testing instantiation of CurrencyConverter class from currency.py
    """
    def test_from_currency_instantiation(self):
        data = 'USD'
        result = CurrencyConverter("USD", "AUD", "2020-01-01")
        self.assertEqual(result.from_currency, data)
    
    def test_to_currency_instantiation(self):
        data = 'AUD'
        result = CurrencyConverter("USD", "AUD", "2020-01-01")
        self.assertEqual(result.to_currency, data)

    def test_date_instantiation(self):
        data = '2020-01-01'
        result = CurrencyConverter("USD", "AUD", "2020-01-01")
        self.assertEqual(result.date, data)

class TestCurrencyCheck(unittest.TestCase): 
    """
    Testing CurrencyConverter class' check_currencies() method in currency.py
    """
    def test_currency_check_False_False(self):
        result = CurrencyConverter("AAA", "AUD", "2020-01-01").check_currencies() & CurrencyConverter("USD", "AAA", "2020-01-01").check_currencies()
        self.assertFalse(result)

    def test_currency_check_False_True(self):
        result = CurrencyConverter("AAA", "AUD", "2020-01-01").check_currencies()
        self.assertFalse(result)

    def test_currency_check_True_False(self):
        result = CurrencyConverter("USD", "AAA", "2020-01-01").check_currencies()
        self.assertFalse(result)

    def test_currency_check_True_True(self):
        result = CurrencyConverter("USD", "AUD", "2020-01-01").check_currencies()
        self.assertTrue(result)

class TestReverseRate(unittest.TestCase):
    """
    Testing CurrencyConverter class' reverse_rate() method in currency.py
    """
    def test_reserve_rate(self):
        self.inverse_rate = 0.719
        self.from_currency = 'USD'
        self.to_currency = 'AUD'
        self.date = '2020-10-10'
        test_converter = CurrencyConverter(self.from_currency, self.to_currency, self.date)
        self.rate = test_converter.get_historical_rate()
        self.assertEqual(test_converter.reverse_rate(), self.inverse_rate)
    
class TestRoundRate(unittest.TestCase): 
    """
    Testing CurrencyConverter class' round_rate() method in currency.py
    """
    def test_round_rate(self):
        self.round_rate = 0.7190
        self.test_number = 0.718999
        self.from_currency = 'USD'
        self.to_currency = 'AUD'
        self.date = '2020-10-10'
        test_converter = CurrencyConverter(self.from_currency, self.to_currency, self.date)
        self.rate = test_converter.get_historical_rate()
        self.assertEqual(test_converter.round_rate(self.test_number), self.round_rate)
    

class TestHistoricalRate(unittest.TestCase):
    """
    Testing CurrencyConverter class' get_historical_rate() method in currency.py
    """
    def test_historical_rate(self):
        self.rate = 1.3908
        self.from_currency = 'USD'
        self.to_currency = 'AUD'
        self.date = '2020-10-10'
        test_converter = CurrencyConverter(self.from_currency, self.to_currency, self.date)
        self.assertEqual(test_converter.get_historical_rate(), self.rate)

if __name__ == '__main__':
    unittest.main()
