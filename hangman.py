import random

#gets list of words
with open('/Users/thomaslee/Desktop/personal projects/hangman/words.txt') as file:
    data = file.read()
    words =[]

    for word in data.split():
        words.append(word)

previous = []
#error message
def error():
    return print("Error! check your input")

#Welcome Function
def welcome():
    if input("Hello! Please press Enter to play a game of Hangman: ") == "":
        return game()
    else:
        error()
        return welcome()
    
#main code
def game():
    word = random.choice(words)
    quiz = ""
    for i in range(len(word)):
        quiz += "-"

   
    count = 10
    attempt =[]
    while count > 0:
         print(quiz)
         guess = input("Guess a letter! You have " + str(count) + "guesses left.")
         
         if guess in attempt:
             print("ERROR \nYou've already tried this letter. Try again")
             count = count

         elif guess in word and guess not in attempt:
             attempt.append(guess)
             for i in range(len(word)):

                 if word[i] == guess:

                     quiz = list(quiz)
                     quiz[i] = guess

                     quiz = "".join(quiz)
                     
             count = count
             print("you got it!")

             if quiz == word:
                 print("Congratulations! You win =) ")
                 break

         
        
         else:
             attempt.append(guess)
             count -= 1
             if count == 0:
                print("Game Over =( \nThe answer was: " + word)
             else:
                print("try again")

#after a round of hangman
def restart():
    question = input("If you'd like to play again, press Enter. If not, press anything else")

    if question == "":
        print("Welcome Back!")
        return game()

    else:
        print("Thank you for playing! Have a good day! :) ")
        



welcome()
restart()



