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

# problem 1
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    counter = 0
    while(counter < len(secretWord)):
        if(secretWord[counter] not in lettersGuessed):
            return False   
        counter += 1
    return True

#print(isWordGuessed('banana', ['z', 'x', 'q', 'a', 'n', 'a', 'n', 'a']))

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    tempSecretWord = ''

    counter = 0
    while(counter < len(secretWord)):
        if(secretWord[counter] in lettersGuessed):
            tempSecretWord += ''.join(secretWord[counter])
        else:
            tempSecretWord += ''.join('_ ')
        counter += 1
    
    return tempSecretWord
#print(getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's']))


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    availableLetters = ''
    counter = 0
    
    while(counter < len(string.ascii_lowercase)):
        if string.ascii_lowercase[counter] not in lettersGuessed:
            availableLetters += ''.join(string.ascii_lowercase[counter])
        counter += 1
    
    return availableLetters
#print(getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']))

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
    arraySecretWord = secretWord
    numLetters = len(secretWord)
    lettersGuessed = []
    NUM_CHANCES = 8
    mistakesMade = 0
    availableLetters = getAvailableLetters(lettersGuessed)
    
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", numLetters, "letters long.")
    print("-------------")
    
    while NUM_CHANCES != mistakesMade:
        print('You have ' + str(NUM_CHANCES - mistakesMade) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        
        previousGuessedWord = getGuessedWord(secretWord, lettersGuessed)
        lettersGuessed = lettersGuessed.insert(input('Please guess a letter: '))
        
        if isWordGuessed(secretWord, lettersGuessed):
            print('Good guess: ' + secretWord)
            print('Congratulations, you won!')
            break;
        elif previousGuessedWord != getGuessedWord(secretWord, lettersGuessed):#se lettersGuessed for um bom palpite e não completar a palavra toda ainda
            print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
        elif lettersGuessed in previousGuessedWord:#se a lettersGuessed já existia:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            mistakesMade += 1
        print('------------')            

    if NUM_CHANCES == mistakesMade:
        print('Sorry, you ran out of guesses. The word was else.')
    


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()
secretWord = "perivaldo"
hangman(secretWord)



#The output of a winning game should look like this...
#
#
#	Loading word list from file...
#	55900 words loaded.
#	Welcome to the game, Hangman!
#	I am thinking of a word that is 4 letters long.
#	-------------
#	You have 8 guesses left.
#	Available letters: abcdefghijklmnopqrstuvwxyz
#	Please guess a letter: a
#	Good guess: _ a_ _
#	------------
#	You have 8 guesses left.
#	Available letters: bcdefghijklmnopqrstuvwxyz
#	Please guess a letter: a
#	Oops! You've already guessed that letter: _ a_ _
#	------------
#	You have 8 guesses left.
#	Available letters: bcdefghijklmnopqrstuvwxyz
#	Please guess a letter: s
#	Oops! That letter is not in my word: _ a_ _
#	------------
#	You have 7 guesses left.
#	Available letters: bcdefghijklmnopqrtuvwxyz
#	Please guess a letter: t
#	Good guess: ta_ t
#	------------
#	You have 7 guesses left.
#	Available letters: bcdefghijklmnopqruvwxyz
#	Please guess a letter: r
#	Oops! That letter is not in my word: ta_ t
#	------------
#	You have 6 guesses left.
#	Available letters: bcdefghijklmnopquvwxyz
#	Please guess a letter: m
#	Oops! That letter is not in my word: ta_ t
#	------------
#	You have 5 guesses left.
#	Available letters: bcdefghijklnopquvwxyz
#	Please guess a letter: c
#	Good guess: tact
#	------------
#	Congratulations, you won!
#
#    
#
#And the output of a losing game should look like this...
#
#
#	Loading word list from file...
#	55900 words loaded.
#	Welcome to the game Hangman!
#	I am thinking of a word that is 4 letters long
#	-----------
#	You have 8 guesses left
#	Available Letters: abcdefghijklmnopqrstuvwxyz
#	Please guess a letter: a
#	Oops! That letter is not in my word: _ _ _ _
#	-----------
#	You have 7 guesses left
#	Available Letters: bcdefghijklmnopqrstuvwxyz
#	Please guess a letter: b
#	Oops! That letter is not in my word: _ _ _ _
#	-----------
#	You have 6 guesses left
#	Available Letters: cdefghijklmnopqrstuvwxyz
#	Please guess a letter: c
#	Oops! That letter is not in my word: _ _ _ _
#	-----------
#	You have 5 guesses left
#	Available Letters: defghijklmnopqrstuvwxyz
#	Please guess a letter: d
#	Oops! That letter is not in my word: _ _ _ _
#	-----------
#	You have 4 guesses left
#	Available Letters: efghijklmnopqrstuvwxyz
#	Please guess a letter: e
#	Good guess: e_ _ e
#	-----------
#	You have 4 guesses left
#	Available Letters: fghijklmnopqrstuvwxyz
#	Please guess a letter: f
#	Oops! That letter is not in my word: e_ _ e
#	-----------
#	You have 3 guesses left
#	Available Letters: ghijklmnopqrstuvwxyz
#	Please guess a letter: g
#	Oops! That letter is not in my word: e_ _ e
#	-----------
#	You have 2 guesses left
#	Available Letters: hijklmnopqrstuvwxyz
#	Please guess a letter: h
#	Oops! That letter is not in my word: e_ _ e
#	-----------
#	You have 1 guesses left
#	Available Letters: ijklmnopqrstuvwxyz
#	Please guess a letter: i
#	Oops! That letter is not in my word: e_ _ e
#	-----------
#	Sorry, you ran out of guesses. The word was else. 
#    
#

