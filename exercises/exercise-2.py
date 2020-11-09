# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

phrase= input("Please enter a phrase or the word 'quit' to exit: ")   
while phrase != "quit":
    print("What you entered is " + str(len(phrase)) + " characters long")
    phrase= input("Please enter a phrase or the word 'quit' to exit: ")   
else: 
    print("See ya later!")
   
   

