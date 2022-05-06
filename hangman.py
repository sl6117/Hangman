import random

#gets list of words
with open('/Users/thomaslee/words.txt') as file:
    data = file.read()
    words =[]

    for word in data.split():
        words.append(word)

previous = []
#error message
def error():
    #if new word is in previous:
        #return "You have already tried this word"
    return "Error! check your input"

#Welcome Function
def welcome():
    welcome = input("Hello! Please press Enter to play a game of Hangman: ")
    pass