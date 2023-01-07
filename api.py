import requests
import sys

def call_get(url: str) -> requests.models.Response:
    """
    Function that will call the API endpoint (input parameter) and return its response as a requests.models.Response object
    If error, the program will exit and display an error message

    Parameters
    ----------
    URL : str
        Target URL to extract information

    Pseudo-code
    ----------
    Retrive information from the targeted URL and store it to a variable
    IF retrival status is as expected
        return the result
    OTHERWISE
        DISPLAY error message
        THEN exit the program

    Returns
    -------
    str
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response
    else:
        print("There is an error with Frankfurter API")
        sys.exit()

