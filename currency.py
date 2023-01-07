import sys
from frankfurter import Frankfurter

class CurrencyConverter:

    """
    Class to convert currency. It will be used to store arguments from user (currency codes and date) and other information (amount, rate, inverse rate, instantiation of Frankfurter class).

    Attributes
    ----------
    from_currency : str
        Code for original currency
    to_currency : str
        Code for target currency
    amount : float
        Amount (in original currency) to be converted
    rate : float
        Conversion rate (original -> target)
    inverse_rate : float
        The inverse rate of the original conversion rate  (original -> target)
    date : str
        Determine conversion rate based on specific time
    api : Frankfurter
        Instance of Frankfurter class
    """
    def __init__(self, from_currency, to_currency, date):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.amount = None
        self.rate = None
        self.inverse_rate = None
        self.date = date
        self.api = Frankfurter()
        
    def check_currencies(self):
        """
        Method to check if currency codes stored in class attributes are valid.
        Otherwise the program will exit and display invalid message

        Parameters
        ----------
        None

        Pseudo-code
        ----------
        IF both currency 1 and currency 2 are not valid THEN
            DISPLAY error message
        IF currency 1 is not valid THEN
            DISPLAY error message
        IF currency 2 is not valid THEN
            DISPLAY error message
        OTHERWISE
            RETURN True

        Returns
        -------
        str
            Error message
        """
        if self.api.check_currency(self.from_currency) == False & self.api.check_currency(self.to_currency)==False:
            print(f"{self.from_currency} and {self.to_currency} are not valid currency codes")
            return False
            sys.exit()
        elif self.api.check_currency(self.from_currency) == False:
            print(f"{self.from_currency} is not a valid currency")
            return False
            sys.exit()
        elif self.api.check_currency(self.to_currency) == False:
            print(f"{self.to_currency} is not a valid currency")
            return False
            sys.exit()
        else:
         return True

    def reverse_rate(self):
        """
        Method to calculate the inverse rate of value stored in the class attribute, round it to 4 decimal places and save it to class attribute

        Parameters
        ----------
        None

        Pseudo-code
        ----------
        Assign a variable to calculate the inverse rate
        Assign a variable to round decimals in the value
        Return the final value

        Returns
        -------
        Float
            Return inverse rate
        """
        self.inverse_rate = 1/self.final_rate
        self.inverse_rate = self.round_rate(self.inverse_rate)
        return self.inverse_rate

    def round_rate(self, rate):
        """
        Method to round value to 4 decimals

        Parameters
        ----------
        rate
            number to be rounded up or down

        Pseudo-code
        ----------
        Round value to 4 decimals and return the result

        Returns
        -------
        Float
            Return rounded number
        """
        return round(rate, 4)

    def get_historical_rate(self):
        """
        Method to call Frankfurter API and extract historical conversion rate for provided currencies (rounded to 4 decimals) and date stored in the class attributes.
        Then it will calculate the inverse rate and will exit by displaying message containing conversion result

        Parameters
        ----------
        None

        Pseudo-code
        ----------
        Extract historical rate from Frankfurter API based on arguments inputted
        Extract exchange and inverse rate based on currencies and date provided then assign the result to a variable
        Display message containing currency 1, currency 2, date, resulting exchange rate and inverse rate

        Returns
        -------
        Str
            Display message containing information requested
        Float
            Exchange rates are included in the message displayed
        """
        self.historical_rate = self.api.get_historical_rate(self.from_currency, self.to_currency, self.date)
        self.final_rate = self.historical_rate.get('rates').get(self.to_currency)
        print(f'The conversion rate on {self.historical_rate.get("date")} from {self.from_currency} to {self.to_currency} was {self.final_rate}. The inverse rate was {self.reverse_rate()}') 
        return self.final_rate
