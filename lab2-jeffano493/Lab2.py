# Add your code here
with open("Optimism_and_your_health.txt", "r") as file:
    info = file.read()
    words = info.split()

    #Creates a list called wordsLengths so the words are stored by the lengths
    wordsLengths = {}
    
    for word in words:
        # Cleans up the word, goes through every character and add its to a new list if it is alphanumeric
        # Once its been added, it will use the join method to add the characters back
        cleaned_up_word = ''.join([char for char in word if char.isalnum()])
        
        #It checks if the length of the cleaned up word is already in the list of wordsLengths
        if len(cleaned_up_word) in wordsLengths:
            #if it is already there, then it will just append the cleaned-up word to the list of words with the same length by using 
            wordsLengths[len(cleaned_up_word)].append(cleaned_up_word)
        else:
            #if it is not already there, a new key in the dictionary with the length as the key, and a list containing the cleaned-up word as the value by using 
            #wordsLengths[key] = [value]
            #key = the length of the cleaned up word
            #value = the cleaned up word
            wordsLengths[len(cleaned_up_word)] = [cleaned_up_word]

    #Finds the max key and saves it
    maxLength = max(wordsLengths.keys())   #set this variable to the max. length
    
    #Using the max length, prints the appened list of the all the words with that length
    wordsWithMaxLen = wordsLengths[maxLength] #set this variable to list of words corresponding to the max. length

# Please don't change the following two lines
print("Max. Length:" + str(maxLength) + " =>")
print(wordsWithMaxLen)