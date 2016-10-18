#import the random module
import random
#store words for the user to choose from
word_bank = ["eat", "cat",'dog','bat']
#chose a random word from the word bank
py_word = random.choice(word_bank)
#make a list to store blanks 
dummy = []
#fill the dummy list with ! equivalent to the number of letters in the word

for i in range(len(py_word)):
    dummy += "!"
dummy_string = ''.join(dummy)

print(dummy_string)    
#print(dummy)


#make a list with the user input 
store_user = ''
#set an accumulator variable set to zero tracking the number of guesses the user makes
wrong_guesses = 0
# the user gets to guess 2 more times than there are letters in the word
number_guess = len(py_word) + 1
#set an accumulator variable for correct guesses
right_guesses = 0
#as long as the number of guesses is lower than the length of the word+2 keep accepting input

        
    
    
     
    

turns = number_guess - (wrong_guesses + right_guesses)
while turns > 0 or (store_user != py_word):
    #accept input from the user
    user = (input("Enter a letter: "))
    if user == "":
        print("you must enter a letter!")
    store_user += user
    turns = number_guess - (wrong_guesses + right_guesses)
    
    if turns > 0:
        print("You have", turns, "chances to guess this word.")
    if turns == 0:
        print("you ran out of guesses, the word is ", py_word)
        break
    #if the user input has every letter that is in the py_word, the user wins the game
    if store_user == py_word:
        turns = 0
        print("Congrats!, you got it")
        break
    #found uses the find method for strings to take the user input string character and find the string position in the word it is a part of
    found = py_word.find(user)
    #since found is an int value, letter is the actual alphanumeric letter in the position of the index in found at py_word
    letter = py_word[found]
    
    #found will return -1 if the letter in letter isn't in an indexed position in the word, therefore when the int value of found returns a number that isn't -1     
    if found != -1 and user != "":
        right_guesses = right_guesses + 1
        #if the value of the index stored in found is not negative 1, the letter value is the alphanumeric char located in the index of found in py_word
        
    elif  found == -1 or user == '':
        #otherwise, if found does = -1 accumulate the trial guess into a list of wrong guesses
        wrong_guesses = wrong_guesses + 1
        print(" The letter isn't in the word!")
    
    if found != -1 and user != '':
        #additionally, if found is non negative and the value of the alphanumeric character is actually in the word, change the ! in dummy to the character in the found position in py_word
        dummy[found] = letter
        #reset count to zero if the user gets a correct letter
  

    #print the dummy list as a string of exclamation marks so it doesn't look like a list.     
    print(' '.join(dummy))



    
    #fix len of chances with right and wrong guesses 



    
