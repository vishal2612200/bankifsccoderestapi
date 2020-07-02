# bankisfccoderestapi

# Database
 Postgresql
 
# Database File
indian_banks.sql

# Rest API Implementation
Django Rest-Framework

# Environment / Deployment
Heroku

# URLs
   ##  Get bank details with given ifsc
 - https://bankifsccoderestapi.herokuapp.com/api/bank/<isfc-code>/
  
   ## Get bank details with given bank-name and city
 - https://bankifsccoderestapi.herokuapp.com/api/bank?name=<bank-name>&city=<city>&limit=<limit-number>&offset=<offset-number>
   
   ## Get the list of all bank details
 - https://bankifsccoderestapi.herokuapp.com/api/bank/?limit=<limit-number>&offset=<offset-number>

# Programming Language 
Python

# How to test the rest api?

Step - 1) Download the test/curl_examples.sh file into your local computer.
Step - 2) Open down your terminal and run 'sh curl_examples.sh'

# Results
![bankisfccoderestapi result](https://user-images.githubusercontent.com/37480057/86409538-b130a580-bcd6-11ea-9914-bbd1355093b7.png)
