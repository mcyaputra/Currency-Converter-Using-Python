import datetime
import sys

def check_arguments(args):
    """
    Function to check if there are enough argument provided (in this case, exactly 3) and return the argument if it checks out.
    Otherwise program exits and displays error message.

    Parameters
    ----------
    args
        argument to be checked

    Pseudo-code
    ----------
    IF number of arguments < 3 THEN
        display error message
        AND exit the program
    OTHERWISE
        IF the arguments provided equal three arguments THEN
        RETURN the arguments
    
    Returns
    -------
    str
        Return argument after checking
    """
    if len(args) != 3 :
        print("[ERROR] You need to provide 3 arguments in the following order: <date> <currency1> <currency2>")
        sys.exit()
    else:
        return args

def check_date(date):
    """
    Function to check if provided date is valid and return "True" if valid. 
    Otherwise the program exits and displays invalid message.

    Parameters
    ----------
    Date
        check if value is a valid date

    Pseudo-code
    ----------
    Define the expected date format, assign to a variable
    If value is a date and right format
        return TRUE
    OTHERWISE
        DISPLAY error message
        AND exit the program

    Returns
    -------
    Bool
        True if format is valid
        Otherwise display error message
    """
    date_format = '%Y-%m-%d'
    try :
        date_entered = datetime.datetime.strptime(date, date_format)
        return True
    except: 
        print("Provided date is invalid")
        sys.exit()
