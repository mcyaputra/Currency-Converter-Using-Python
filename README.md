## 💲 Currency Converter

This python scripts pull exchange rates from Frankfurter API, which tracks rates published by European Central Bank (ECB). It is capable of showing exchange rate between two currencies at a specified date as well as their inverse rate.

Simply provide 3 arguments:
1. Date
2. From currency
3. Target currency

The script will tell you what is the exchange rate between the two currencies specified for the date you specified

Some additional features to be added:

-Real time exchange rate, counting down to the seconds

-Showing exchange rate based on a value entered by user

-Make predictions of future exchange rates

-Provide recommendation if user should exchange or hold on to their currency

## 🤖 How to Setup

1. Download all of the following files: 
-[main.py](/main.py)
-[checks.py](/checks.py)
-[currency.py](/currency.py)
-[frankfurter.py](/frankfurter.py)
-[api.py](/api.py)

2. Save all files in one working folder of your choice

## 💻 How to Run the Program
1. Open terminal and navigate to the working folder where all the files were stored
2. Run main.py file in the terminal by typing:  
python (or python3 on macbook) <file name> <YYYY-MM-DD> <from_currency> <to_currency>  

-Result should display the exchange rate and inverse rate based on currency codes and date 

3. To run unittest, download the following files:  
-[test_api.py](/test_api.py)
-[test_checks.py](/test_checks.py)
-[test_currency.py](/test_currency.py)
-[test_frankfurter.py](/test_frankfurter.py)

4. Run every test files individually in the terminal and check the result
  
## ⚙️ Package/library used:  
-sys  
-datetime  
-requests (version 2.28.1)  
-unittest

## 💡 Project Structure
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

## 👨 Feedback/Ideas? Lets connect!

I would love to hear feedbacks or ideas from you! Or just simply connect and chat, feel free to contact me on:

<a href="https://www.linkedin.com/in/michaelyaputra/">
    <img align="left" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg"/>

</a>

<a href="https://github.com/mcyaputra">
    <img align="left" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/github.svg" />

</a>


