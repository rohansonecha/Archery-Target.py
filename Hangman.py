# Author: Rohan Sonecha
# hangman.py
# creates the hangman game
import random

dictionary = open("dictionary.txt", "r").readlines()
randomSpot = random.randint(0, len(dictionary))
word = dictionary[randomSpot].strip()
print("I'm thinking of a word that is ",len(word)," letters long.")


def contains(word):
    n = len(word)
    lives = 6
    lettersToDisplay = "_ " * n
    lcount = 0
    letterguessed = []
    print ("Lives: ", lives)
    print("What you have so far: ", lettersToDisplay)
    if (lives == 0):
        print (word)
    while(lives > 0):
        print("You have guessed ",letterguessed)
        print("printing the man:")
        if (lives == 6):
            print(" 0 ")
        elif (lives == 5):
            print("\\0 ")
        elif (lives == 4):
            print("\\0/")
        elif (lives == 3):
            print("\\0/")
            print(" | ")
        elif (lives == 2):
            print("\\0/")
            print(" | ")
            print("/  ")
        elif (lives == 1):
            print("\\0/")
            print(" | ")
            print("/ \ ")
        guessWord = input("Would you like to guess the word[y/n]? ")
        if (guessWord == "y"):
            userguessw = input("What is the word: ")
            if (userguessw == word):
                print ("You are correct")
                return True
            else:
                print ("You are incorrect")
                lives -= 1
                print ("Lives: ", lives)
        else:
            userguessl = input("Guess a new letter: ")
            lcount = 0
            if(userguessl in word):
                for letter in word:                   
                    if (userguessl == letter):
                        break
                    else:
                        lcount += 1
                print ("There is a: ", userguessl)
                lettersToDisplay = lettersToDisplay[0:lcount] + userguessl + lettersToDisplay[lcount+1:]
                print("What you have so far: ", lettersToDisplay)
                if (lettersToDisplay == word):
                    print ("You are correct")
                    return True                        
            else:
                print ("There is no: ", userguessl)
                letterguessed = letterguessed.append(userguessl)
                print("What you have so far: ", lettersToDisplay)
                lcount += 1
                lives -= 1
                print ("Lives: ", lives)
contains(word)
