"""
Anthony Porporino
Veronique Godin
Computer Assignment
May 2018
"""
from Help import *
from random import *


#PART 1: SETTING UP RSA

def get_integer(string):
    #Given the string used to ask the user, this function returns the user's chosen integer
    #This function was made so that it won't crash if the user enters a letter
    while True:
        answer = input(string)
        try:
            A = int(answer)
            break
        except ValueError:
            print("\n",answer, "is not an integer\n")
    return A

def PickPrimes():
    """This function allows the user to see a list of primes between two of their chosen numbers and returns
    2 primes that they choose"""
    while True:
        p_min = get_integer("Choose the minimum prime you wish to have as long as it is >= 2627. ")
        p_max = get_integer("Choose maximum prime you wish to have, making sure it is greater than your minimum. ")
        if (p_min >= 2627) and (p_max > p_min): #Makes sure the min prime is > 2627 and that the max prime is > the min prime
            break
        else:
            print("Either your min is less than 2627 or your max is less than your min")
    lst = ListPrime(p_min,p_max) #Uses Help file function to get list of all the primes in between min and max
    print("Here is a list of primes in between your min and max: ", lst)
    while True:
        Prime_p = get_integer("Now, choose a prime") #Now user picks their 2 primes
        Prime_q = get_integer("Choose another prime")
        is_prime = Prime(Prime_p)
        is_prime2 = Prime(Prime_q)
        if (Prime_p != Prime_q) and (is_prime and is_prime2): #Makes sure they are actually prime and they do not equal each other
            return (Prime_p, Prime_q)
        else:
            print("Either your prime numbers are the same or one of them isn't prime. Choose again")
    
    
def RandomPickPrimes():
    """This function allows the user to see a list of primes between two of their chosen numbers and returns
    2 randomly generated primes from that list"""
    while True:
        p_min = get_integer("Choose the minimum prime you wish to have as long as it is >= 2627. ")
        p_max = get_integer("Choose maximum prime you wish to have, making sure it is greater than your minimum. ")
        if (p_min >= 2627) and (p_max > p_min) and (len(ListPrime(p_min,p_max)) > 1): #Makes sure the min prime is > 2627, that the max prime is > the min prime and that there is at least one prime in between
            break
        else:
            print("Either your min is less than 2627, your max is less than your min or there are no prime numbers in between the numbers you chose. Try again")
    lst = ListPrime(p_min,p_max) #Uses Help file function to get list of all the primes in between min and max 
    while True:
        randomPrime_p = lst[randint(0, len(lst) - 1)] #Randomly chooses 2 primes using the random module
        randomPrime_q = lst[randint(0, len(lst) - 1)] 
        if randomPrime_p != randomPrime_q: #Makes sure that the 2 primes are not equal
            return randomPrime_p, randomPrime_q
        
def SetUp():
    """This function runs either PickPrimes or RandomPickPrimes based on the users choice. It then asks
    for the user to pick a power e and returns the public key: n, e and the private key d which is the
    inverse of e mod phi_n"""
    while True: #Asks user to choose if they would like to pick their primes or have them randomly picked
        choice = get_integer("Enter 1 if you would like to choose your primes or 2 if you would like it to be random")
        if choice == 1:
            p, q = PickPrimes() #Runs PickPrimes function
            break
        elif choice == 2:
            p, q = RandomPickPrimes() #Runs RandomPickPrimes function
            break
        else:
            print("Not valid input, please try again.")
    print("The primes are: ", p, q)
    n = p*q #Calculates the value n (an element of the public key)
    phi_n = (p - 1)*(q - 1) #Calculates phi_n 
    while True: #Asks user to choose a value for e (second element of the public key)
        e = get_integer("\nChoose an integer to be the power e. If you would like the decryption to be difficult do not choose e to be 1")
        if RelativelyPrime(e, phi_n) and Inverse(e,phi_n): #Makes sure the e and phi_n are relatively prime and that there is an inverse for e mod phi_n
            break
        else:
            print("E is not relatively prime to phi_n: ", phi_n, "or there is no inverse of e mod phi_n, please try again")
    d = Inverse(e, phi_n)
    return (n,e,d)

#PART 2: ENCODING MESSAGES

def GetMessage():
    #This function allows the user to create a message containing a list of single letter strings without crashing
    Message = []
    while True:
        answer = input("Choose a letter to add or enter 1 to stop adding letters")
        try: #Makes sure that user enetered a letter or if they enetered 1 it will break
            A = int(answer)
            if (answer == "1"):
                break
            else:
                print(answer, "is not a letter, try again.")
        except ValueError:
            if len(answer) == 1: #Ensures user enters the letters one at a time
                Message.append(answer)
            else: print("You must add letters one at a time")
    if (len(Message) % 2) == 1: #If the message has an odd number of letters this will add a space at the end to make it an even number
        Message.append(" ")
    return Message
    

def LetterToNumber(Message):
    """Given a list of single letter strings, this function will change each letter
    to it's corresponding number in the alphabet and then return a list containing those numbers"""
    MessageInNumber = []
    for i in Message:
        try:
            MessageInNumber.append(Number[i]) #Using the Number dictionary from the Help file
        except KeyError: #If the letter is not found it means the user entered a non-letter non-number character and this treats it like a space
            print("The non letter character you inputed will be treated as a space")
            MessageInNumber.append(0)
    return MessageInNumber #List of numbers corresponding to letters from the message

        

def Encode(Message,n,e):
    """This allows the user to encode their message given the actual message (a list of single letter strings)
    and the variables n and e (relatively prime to n)"""
    InNumber = LetterToNumber(Message) #Changes list of letters to numbers
    Coded = []
    while InNumber: #easier way of saying while InNumber is not empty
        x = InNumber.pop(0) #Takes the first number in the list
        y = InNumber.pop(0) #Takes the second number in the original list
        if x == 0: #If a space is entered at an odd index, this will disregard it and append the encoded value of y
            Coded.append(pow(y,e,n))
        else:
            NumberToEncrypt = 100*x + y #This allows us to encrypt 2 letters in one number
            Coded.append(pow(NumberToEncrypt,e,n)) #Encodes the number to make it difficult to decrypt
    return Coded #List of numbers containing the encrypted message

#PART 3: DECODING MESSAGES

def GetMessageNumber():
    """This function allows the user to create a list of numbers to decrypt without crashing"""
    Code = []
    while True:
        answer = input("Enter the numbers of the code you want to decrypt enter the letter: 'a' when you are finished")
        try:
            A = int(answer)
            Code.append(A)
        except ValueError: #Checks if the input is "a" to break or ensures that the user does not enter a letter
            if answer == 'a':
                break
            else: print("Not valid input")
    return Code #List of numbers to decrypt

def NumberToLetter(Message):
    """Given a list of numbers between 1 and 26 this function will return a list of the corresponding letters
    to those numbers"""
    Letters_list = []
    for i in Message:
        Letters_list.append(Letter[(i)]) #Uses the help file diction Letter to find switch numbers to letters
    return Letters_list

def Decode(Message,n,d):
    """Given the message (a list of numbers) and the variable n and d (private key)
    this function will return the decrypted message as a list of letters"""
    Decoded = [] 
    while len(Message): #While message is not empty
        number = pow(Message.pop(0),d,n) #This decrypts the number to another number that corresponds to 2 letters
        y = number%100 #This will give the number relating to the second letter
        x = (number - y) // 100 #This will give the number relating to the first letter
        Decoded.append(x)
        Decoded.append(y)
        if (x < 27) and (y < 27): #Checks to make sure that the numbers actually correspond to a letter
            continue
        else:
            return "There is no message corresponding to those number"
    return NumberToLetter(Decoded)#List containg the decrypyted message

#PART 4: CORE

#Intro to welcome user and explain what the program does
print("""Hello and welcome to the program. This program will allow you to encrypt and decrypt
messages using RSA cryptography. To start, we have to set up the encryption process by choosing 2 primes. Please follow the prompts. \n""")
#Set up RSA 
n,e,d = SetUp()

#Menu to allow user to choose what they would like to do
while True:
    user_choice = get_integer("""Enter the number corresponding to what you would like to do
1.) Set up RSA again.
2.) Encrypt a message.
3.) Decrypt a message
4.) Print the public key (n, e).
5.) Print the private key d.
6.) Leave.""")
    if user_choice == 1:
        n,e,d = SetUp()
    if user_choice == 2:
        print("\nFollow the prompts to tell me the message you would like to encrypt\n")
        print("\nThe encoded message is: ", Encode(GetMessage(),n,e), "\n")
    if user_choice == 3:
        print("\nFollow the prompts to tell me the code you would like to decrypt\n")
        print("\nThe decoded message is: ", Decode(GetMessageNumber(),n,d), "\n")
    if user_choice == 4:
        print("\nThe public key (n,e) is: ", n, e, "\n")
    if user_choice == 5:
        print("\nThe private key is (d) is: ", d, "\n")
    if user_choice == 6:
        break

    
        
    
