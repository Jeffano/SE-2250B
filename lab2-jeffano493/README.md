[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9826953&assignment_repo_type=AssignmentRepo)
# Lab 2: Built-In Collections and Loops

## The problem
- Find all the words that have the maximum length in the given text file.
- The calculation of the length of the words should not include any special characters (e.g. if 'Hello!' is part of the text, the exclamation mark (!) shouldn't be counted, and if the word "don't" is in the text the apostrophe (') shouldn't be counted)
- Follow the steps in the algorithm below (I understand that there are other ways to do the same action; however, the objective is to practice working with certain concepts, not to solve the problem in general)

## The Algorithm
This problem can be solved with only one pass over the words in the file.

- look-up the open() function to learn how to open a file and read its content and use it to open the given text file.
- Figure out the function that allows us to turn the file's text into a list of words.
- Create an empty dictionary to construct in the following loop. The dictionary would contain the available lengths as keys that map to lists of words that correspond to the length in the key.
- For each word in the list:
    - Use list comprehension to put the characters of the word in a list as long as the characters are alphanumeric. There's a function in str that allows you to check whether the character in a string is alphanumeric; find this function and use it to create the list, then put the characters back together as a cleaned-up string.
    - if the length of the current cleaned-up word is already in the dictionary, add that cleaned-up word to the corresponding length; else, add a new entry with the word's length as the key and a one-element list containing the word as the value.
- After exiting the loop, use the max function to find the maximum key and the corresponding list of words.

## Expected Output

Max. Length:17 => 

['rehospitalization']
