import sys
from currency import CurrencyConverter
from checks import check_arguments, check_date

def main():
    """
    Main logic of the program.
    -Argument entry point
    -Argument validity and format checks
    -Run API and extract result 

    Parameters
    ----------
    args
        argument from user

    date
        date input from user

    Pseudo-code
    ----------
    User enters argument in python and save it to a variable
    Checks if argument entered is valid

    Extract date from argument and save it to a variable
    Checks if date entered is valid

    Initiate CurrencyConverter class using argument as class variable

    Checks if currency codes entered are valid

    Extract and display conversion rate result

    Returns
    -------
    Str
        Return the argument after checking
    Bool
        True if format is valid
        Otherwise Display error message
    Str
        Error message
    Str
        Display message containing information requested
    Float
        Exchange rates are included in the message displayed

    """
    args = sys.argv[1:]
    check_arguments(args)

    date = args[0]
    check_date(date)

    r = CurrencyConverter(args[1], args[2], args[0])

    r.check_currencies()

    r.get_historical_rate()

if __name__ == "__main__":
    print("Launching App")
    main()