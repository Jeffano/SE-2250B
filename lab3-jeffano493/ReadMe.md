[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9927331&assignment_repo_type=AssignmentRepo)
# Lab 3: Functions & OOPs

## Date and DateTime Classes definitions
-	Create a class Date that has three attributes (day, month, and year) initialized through the constructor.
-	Add a definition for the built-in __str__ method so that it would return a string with the format following format ‘day:&lt;day-value>,month:&lt;month-value>,year:&lt;year-value>’ 
    -	e.g. ‘day:1,month:3,year:2020’
    -	for simplicity assume that all value are strings
-	Create a class DateTime that inherits from Date date and adds the attributes representing the hours minutes and seconds that are also initialized in through the constructor of the DateTime class.
-	Override the definition of __str__ with an implementation that utilizes the definition in the parent and concatenates the time components to it with the format 
‘day:&lt;day-value\>,month:&lt;month-value\>,year:&lt;year-value\>--&lt;hrs\>:&lt;mins\>:&lt;secs\>
    -	E.g. 'day:1,month:3,year:2020--11:22:33'

## Date Parsers
-	Define a stand-alone function that receives one argument representing one of the known date formats and returns a function object that remembers the specified format. 
-	The three date formats that can be handled are as follows:
    -	Big-endian (year, month, day), e.g. 2021-03-31
    -	Little-endian (day, month, year), e.g. 31-03-2021
    -	Middle-endian (month, day, year), e.g. 03-31-2021
-	The actual parser function that would be returned can receive an arbitrary number of strings of dates to parse them according to the format that was specified beforehand and return a list of Date objects representing the given dates.

## Testing
-   Please use the names bigEndianParser, littleEndianParser, and middleEndianParser to refer to the corrsponding parser functions as these are the names used for testing
-	You can see the test functions with inputs and expected outputs at the end of the script; please don’t change these (if you find any typos or problems with the tests, please let me know so that I fixed in the source)
-	If you would like to run the tests locally before submitting them to the GitHub classroom assignment, you can follow the instructions below:
o	Open the anaconda prompt as an administrator (on Windows) or the terminal on (Mac or linux)
o	Run the command (>pip install -U pytest) to install the pytest library
o	To test the installation run the command (>pytest --version), if it was correctly installed, you should see the version of pytest printed
o	Change directory to where the Lab3.py is and run the command (>pytest Lab3.py)
