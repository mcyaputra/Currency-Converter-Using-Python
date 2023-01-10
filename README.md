# <Python Currency Converter>

## Author
Name: Michael Yaputra  

## Description

Python currency converter - this program pulls exchange rates from Frankfurter API, which tracks rates published by European Central Bank (ECB). It is capable of showing exchange rate between two currencies at a specified date as well as their inverse rate.

Some additional features to be added:
-Real time exchange rate, counting down to the seconds
-Showing exchange rate based on a value entered by user
-Make predictions of future exchange rates
-Provide recommendation if user should exchange or hold on to their currency

## How to Setup
How to run the program:

1. Download all of the following files: 
1. main.py  
2. checks.py  
3. currency.py  
4. frankfurter.py  
5. api.py  

-To run the converter -> run main.py file in the terminal by typing:  
python (or python3 on macbook) <file name> <YYYY-MM-DD> <from_currency> <to_currency>  

-Result should display the exchange rate and inverse rate based on currency codes and date 

2. To run unittest, open the following files:  
1. test_api.py  
2. test_checks.py  
3. test_currency.py  
4. test_frankfurter.py  

-run every file individually, test should run automatically on every file
  
Package/library:  
-sys  
-datetime  
-requests (version 2.28.1)  
-unittest

## How to Run the Program
In the terminal, run: python (or python3 on macbook) followed by <file name> <date> <from_currency> <to_currency>
Make sure the path is correct, ie the file is at the end of the selected path

## Project Structure
List of files:  
1. main py: this is the main file where the program will be based and run  
2. checks.py: file containing classes to check whether the arguments supplied are valid  
3. currency.py: file containing classes to extract the list of validated currency list, calculate the exchange and inverse rate and provide the intended result  
4. frankfurter.py: file containing classes to call the relevant URLs or endpoints  
5. api.py: file containing a class to make API calls  
6. test_checks.py: file containing scripts to run tests in checks.py making sure the codes are running and returning the expected results  
7. test_currency.py: file containing scripts to run tests in currency.py making sure the codes are running and returning the expected results  
8. test_frankfurter.py: file containing scripts to run tests in frankfurter.py making sure the codes are running and returning the expected results  
9. test_api.py: file containing scripts to run tests in api.py making sure the codes are running and returning the expected results  
10. README.md: markdown file containing project description, functions, scripts, classes and detailed instructions on how to run the program


