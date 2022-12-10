import sys
from currency import CurrencyConverter
from checks import check_arguments, check_date

if __name__ == "__main__":
    print("Launching App")

"""
Main logics of the program.

Pseudo-code
----------
Extract the input arguments
Remove the first argument (name of Python script)
Check there are 3 items in the remaining list of argument (using your defined check_arguments() function)
Check the validity of the input date (using your defined check_date() function)
Instantiate an objet from your defined CurrencyConverter class with the verified 2 currency codes and date
Check the validity of the 2 currency codes (using your defined check_currencies() method from CurrencyConverter class)
Extract the historical rate and calculate its inverse rate (using your defined get_historical_rate() method from CurrencyConverter class)
"""
args = sys.argv[1:]
check_arguments(args)

date = args[0]
check_date(date)

r = CurrencyConverter(args[1], args[2], args[0])

r.check_currencies()

r.get_historical_rate()



   
