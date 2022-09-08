All tests and examples have been run using python3  

Please make sure you have the following python packages:  
tinyDB  
Flask  
json  
requests  
threading  
abc  

To run the example begin by starting the DataService:  
python3 DataService.py  
once the backend is running you can use the sample_usage file to run a simple demo of the project:  
python3 sample_uasge.py

NOTE:
course dates are represeted as an int in format YYMMDD

TODO:  
improved error handling  
improved unit testing - dataservice and businescontroller lack testing
implement better system for managing student and course IDs, for now just using hash()  
improve logic for checking date/time conflicts of courses (assumes courses can not be multiple days for now)  
implement better system for representing course dates and times