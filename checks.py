import datetime
import sys

def check_arguments(args):
    """
    Function that will check if there are enough input arguments provided (ie exactly 3) and will return the input arguments if it is the case.
    Otherwise the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    args
        argument to be checked

    Pseudo-code
    ----------
    IF number of arguments < 3 THEN
        DISPLAY error message
        AND exit the program
    OTHERWISE
        IF the arguments provided equal three arguments THEN
        RETURN the arguments 
    
    Returns
    -------
    str
        Return the argument after checking
    """
    if len(args) != 3 :
        print("[ERROR] You need to provide 3 arguments in the following order: <date> <currency1> <currency2>")
        sys.exit()
    else:
        return args

def check_date(date):
    """
    Function that will check if the provided date is valid and will return the value True if that is the case. 
    Otherwise the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    Date
        check if the parameter supplies is a valid date

    Pseudo-code
    ----------
    Define the expected date format and assign it into a variable
    IF the date or value supplied is the indeed a date and the right format
        return result as true
    OTHERWISE
        DISPLAY error message
        AND exit the program

    Returns
    -------
    Bool
        True if format is valid
        Otherwise Display error message
    """
    date_format = '%Y-%m-%d'
    try :
        date_entered = datetime.datetime.strptime(date, date_format)
        return True
    except: 
        print("Provided date is invalid")
        sys.exit()

        