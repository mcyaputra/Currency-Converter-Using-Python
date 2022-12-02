import requests
import sys

def call_get(url: str) -> requests.models.Response:
    """
    Function that will call the API endpoint (input parameter) and return its response as a requests.models.Response object
    In case of an error, the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    URL : str
        Target URL to extract information

    Pseudo-code
    ----------
    Retrive information from the targeted URL and store it into a variable
    IF retrival status is as expected by checking the status
        return the result
    OTHERWISE
        DISPLAY error meessage
        AND exit the program

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

