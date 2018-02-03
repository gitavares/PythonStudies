# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    counter = 0
    while(counter < len(secretWord)):
        if(secretWord[counter] not in lettersGuessed):
            return False   
        counter += 1
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    tempSecretWord = ''

    counter = 0
    while(counter < len(secretWord)):
        if(secretWord[counter] in lettersGuessed):
            tempSecretWord += ''.join(secretWord[counter])
        else:
            tempSecretWord += ''.join('_ ')
        counter += 1
    return tempSecretWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetters = ''
    counter = 0
    
    while(counter < len(string.ascii_lowercase)):
        if string.ascii_lowercase[counter] not in lettersGuessed:
            availableLetters += ''.join(string.ascii_lowercase[counter])
        counter += 1
    return availableLetters

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    numLetters = len(secretWord)
    lettersGuessed = []
    NUM_CHANCES = 8
    mistakesMade = 0
    letterTyped = ''
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", numLetters, "letters long.")
    print("-------------")
    
    while NUM_CHANCES != mistakesMade:
        print('You have ' + str(NUM_CHANCES - mistakesMade) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        
        previousGuessedWord = getGuessedWord(secretWord, lettersGuessed)
        previousAvailableLetters = getAvailableLetters(lettersGuessed)
        letterTyped = input('Please guess a letter: ')
                
        if letterTyped[0] in previousGuessedWord or letterTyped[0] not in previousAvailableLetters:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(letterTyped)
            if isWordGuessed(secretWord, lettersGuessed):
                print('Good guess: ' + secretWord)
                print('------------') 
                print('Congratulations, you won!')
                break
            elif previousGuessedWord != getGuessedWord(secretWord, lettersGuessed):
                print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
            else:
                print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
                mistakesMade += 1
        print('------------')            

    if NUM_CHANCES == mistakesMade:
        print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')
    


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)


#secretWord = "amazonas"
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)