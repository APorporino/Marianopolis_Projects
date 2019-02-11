"""Anthony Porporino
Exercise 1: Guessing Game"""
#Question 1
def UserGuesses(x):
    Correct = False
    while Correct == False: #until user guesses correctly it keeps asking
        guess = int(input("Guess a number between 1 and 100"))#this asks the user for his guess
        if guess == x:
            print("You guessed correctly!")
            Correct = True
        if guess < x:
            print("Your guess is too low")
        if guess > x:
            print("Your guess is too high")

#Question 2
def ComputerGuesses(min,max):
    Correct = False 
    print("Guess a number in your head between 1 and 100 and I will guess it")
    while Correct == False: #while loop used to allow computer to keep guessing and once it guessing correctly it will exit the loop
        guess = (min + max) // 2 #initial guess
        print("My guess is", guess)
        userHelp = int(input("Enter 1 if my guess is right, 2 if it is too low, and 3 if its too high")) 
        if userHelp == 1:
            Correct = True
            print("Thanks for playing")
        if userHelp == 2:
            min = guess + 1 #this will change the min to the guess so that the range of possible answer shrinks
        if userHelp == 3:
            max = guess - 1 #this will change the max to the guess so that the range of possible answer shrinks too
#Question 3
from random import randint #alows us to use a random integer
userChoice = int(input("If you want to guess a number hit 1, if you want me to guess a number hit 2")) 
if userChoice == 1: 
    UserGuesses(randint(0,100)) #runs the UserGuesses function
if userChoice == 2:
    ComputerGuesses(0,100) #runs the ComputerGuesses function
            
            
            

   
