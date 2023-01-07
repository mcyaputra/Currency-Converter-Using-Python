from readline import get_history_item
from api import call_get

class Frankfurter:
    """
    Class that manages API calls to Frankfurter. It will be used to store the URLs to relevant endpoints, extract and store available currency codes.

    Attributes
    ----------
    base_url : str
        Base url to Frankfurter API
    currencies_url : str
        Frankfurter endpoint to extract currencies list
    historical_url : str
        Frankfurter endpoint to extract historical currency conversion rates
    currencies: list
        List of available currency codes
    """
    def __init__(self):
        self.base_url = 'https://api.frankfurter.app'
        self.currencies_url = 'https://api.frankfurter.app/currencies'
        self.historical_url = 'https://api.frankfurter.app/latest?to=USD,GBP'
        self.currencies = []
    
    def get_currencies_list(self):
        """
        Method to extract list of available currencies and returns it as a Python list.

        Parameters
        ----------
        None

        Pseudo-code
        ----------
        Call API to retrieve the list of available currencies, return it in a json format and extract the keys only
        Return the result and format it into a list

        Returns
        -------
        List
            List of currencies formatted into python list
        """
        output = call_get(self.currencies_url).json().keys()
        return list(output)

    def check_currency(self, currency):
        """
        Method that will check if currency code provided is valid and return True
        Otherwise it will return False

        Parameters
        ----------
        Currency
            Value to be checked

        Pseudo-code
        ----------
        Retrieve the list of currencies using pre defined method and assign it to a variable
        Check if the argument/currency supplied is in the currency list
        IF argument/currency is in the currency list
            Return True
        IF argument/currency is not in the currency list
            Display an error message saying currency is not valid

        Returns
        -------
        Bool
            Result of valid currency
        Str
            Error message if currency is not valid
        """
        self.currencies = self.get_currencies_list()
        for i in self.currencies:
            if(currency.upper()==i.upper()):
                return True
        else:
            print(f"{currency} is not a valid currency code")
            return False
            

    def get_historical_rate(self, from_currency, to_currency, from_date, amount=1):
        """
        Method to extract historical conversion rate based on specific date and currency. It will return an requests.models.Response object.

        Parameters
        ----------
        from_currency
            Currency 1 / original currency
        to_currency
            Currency 2 / target currency
        from_date
            Exchange rate will be based on this date/value
        amount
            the number of result

        Pseudo-code
        ----------
        Set up the target URL to extract exchange rate and assign it to a variable
        Extract the exchange rate from the URL using pre defined method and assign it to a variable
        Convert the result to json and assign it to a variable
        Return the final result

        Returns
        -------
        dict/json  
            Result will be returned in dictionary format
        """

        self.historical_url = "https://api.frankfurter.app/%(d)s?from=%(f)s"%{'d':from_date,'f':from_currency}
        response = call_get(self.historical_url)
        response_json = response.json()
        return response_json