import sys
from frankfurter import Frankfurter

class CurrencyConverter:

    """
    Class that represents a Currency conversion object. It will be used to store the input arguments (currency codes, date) and also other information required (amount, rate, inverse rate, instantiation of Frankfurter class).

    Attributes
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    rate : float
        The conversion rate to be applied on the origin amount (origin -> destination)
    inverse_rate : float
        The inverse of the previous rate  (destination -> origin)
    date : str
        Date when the conversion rate was recorded
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
        Method that will check if currency codes stored in the class attributes are valid.
        Otherwise the program will exit and display the relevant message provided in the assignment brief

        Parameters
        ----------
        None

        Pseudo-code
        ----------
        IF both currency1 and currency2 are not valid THEN
            DISPLAY error message
        IF currency1 is not valid THEN
            DISPLAY error message
        IF currency2 is not valid THEN
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
        Method that will calculate the inverse rate from the value stored in the class attribute, round it to 4 decimal places and save it back in the class attribute inverse_rate.

        Parameters
        ----------
        None

        Pseudo-code
        ----------
        Set a variable to calculate the inverse rate
        Set a variable to round decimals to the nearest number
        Return the final value

        Returns
        Float
            Return inverse rate
        """
        self.inverse_rate = 1/self.final_rate
        self.inverse_rate = self.round_rate(self.inverse_rate)
        return self.inverse_rate

    def round_rate(self, rate):
        """
        Method that will round an input argument to 4 decimals places.

        Parameters
        ----------
        rate
            number to be rounded up or down

        Pseudo-code
        ----------
        Round number to 4 decimals and return the result

        Returns
        -------
        Float
            Return rounded number
        """
        return round(rate, 4)

    def get_historical_rate(self):
        """
        Method that will call the Frankfurter API and get the historical conversion rate for the currencies (rounded to 4 decimals) and date stored in the class attributes.
        Then it will calculate the inverse rate and will exit by displaying the relevant message provided in the assignment brief

        Parameters
        ----------
        None

        Pseudo-code
        ----------
        Extract historical rate from Frankfurter PI based on the arguments supplied,
        Get the specific target currency and exchange rate, return the exchange rate and the inverse rate based on the date argument, assign the result to a variable
        Display the message with the relevant information including currency1, currency2, date, exchange rate and inverse rate

        Returns
        -------
        Str
            Display message containing information requested
        Float
            Exchange rates are included in the message displayed
        """
        self.historical_rate = self.api.get_historical_rate(self.from_currency, self.to_currency, self.date)
        print(self.historical_rate)
        self.final_rate = self.historical_rate.get('rates').get(self.to_currency)
        print(f'The conversion rate on {self.historical_rate.get("date")} from {self.from_currency} to {self.to_currency} was {self.final_rate}. The inverse rate was {self.reverse_rate()}') 
        return self.final_rate
