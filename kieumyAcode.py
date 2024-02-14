
import random
import re
from wordList import wordList


board = [" ", " ", " ",
        " ", " ", " ",
        " ", " ", " ",
        "~", "~", "~"]
listOfWrongGuesses = []
guessList = []
guessDict = {}
guessCount = 0
wrongGuessCount = 0

def main():

    player1 = input("Hello! What's player1 name?")
    player2 = input("Hello! What's player2 name?")

    instructions(player1, player2)
    
    secret = ''
    secret = getGuess(secret)
    
    snowmanGrid(board)
    blanks = ["_"] * len(secret)
    
    print(*blanks)
    print()

    player = player1
    while(wrongGuessCount < 5 and guessCount < len(secret)):
        if player == player1:
            blanks = fillInBlank(player1, secret, blanks)
            player = player2
        else:
            blanks = fillInBlank(player2, secret, blanks)
            player = player1

    print("Congratulations! The hidden word is ", secret)

    winner  =''
    if player == player1:
        winner = player2
    else:
        winner = player1

    statusReport(winner, wrongGuessCount)

def instructions(player1, player2):
    print(f"Welcome {player1} and {player2} to the Snowman Game!")
    print("You guys will guess the secret word!  Hint: hidden word related to jobs (*'~'*)")
    print("Once you guess wrong, the snowman will be drawn an extra stroke")
    print("Win the game before the snowman is finished!")
    print("Let's start!!")

def getGuess(secret):
    secret = random.choice(wordList)
    return secret

def fillInBlank(player, secret, blanks):
    print("List of Wrong Guesses: ", listOfWrongGuesses)
    inp = input(f"{player} guess the letters in a hidden word: ").lower()
    inp = checkValidInp(inp)
    

    indices_object = re.finditer(pattern=inp, string=secret)
    indices = [index.start() for index in indices_object]

    
    if len(indices) > 0:

        for indice in indices:
            blanks[indice] = inp

        if inp not in guessList:
            global guessCount
            guessList.append(inp)
            guessCount += len(indices)
        

        snowmanGrid(board)
        print(*blanks)
        print()
    else:
        print("Wrong! ", inp, " not in hidden word. Try again!")
        global wrongGuessCount
        wrongGuessCount += 1
        drawSnowman(wrongGuessCount, board)
        snowmanGrid(board)
        
        if inp not in listOfWrongGuesses:
            listOfWrongGuesses.append(inp)
            
        print(*blanks)
        print()

    return blanks


def checkValidInp(inp):
    while True:
        if not inp.isalpha():
            inp = input("Invalid! You only can enter letter. Enter again: ")
        elif inp in listOfWrongGuesses:
            print(f"{inp} have already been guessed!")
            print("List of Wrong Guesses: ", listOfWrongGuesses)
            inp = input("Enter your guessing letter again: ")
        
        elif inp in guessList:
            print(f"{inp} have already been guessed!")
            print("List of Guesses: ", guessList)
            inp = input("Enter your guessing letter again: ")

        else:
            break

    return inp


def statusReport(player, wrongGuessCount):
    if wrongGuessCount >= 5:
        print("No one win the game!")
    else:
        print(f"{player} Win!")

def snowmanGrid(board):
    print("-------------------")    
    print("|  " + board[0] + "  |  " + board[1] + "  |  " + board[2] + "  |")
    print("+-----+-----+-----+")
    print("|  " + board[3] + "  |  " + board[4] + "  |  " + board[5] + "  |")
    print("+-----+-----+-----+")
    print("|  " + board[6] + "  |  " + board[7] + "  |  " + board[8] + "  |")
    print("+-----+-----+-----+") 
    print("|  " + board[9] + "  |  " + board[10] + "  |  " + board[11] + "  |")
    print("-------------------") 

#I haven't figured out how to do it yet so I just write key-value pairs (rowNumber:value)
myDict ={1:[" ", "O", " "],
         2:["/", "O", "\\"],
         3:[" ", "O", " "]}

def drawSnowman(wrongGuessCount, board):

    if wrongGuessCount == 1:
        board[1] = "O"
    elif wrongGuessCount == 2:
        board[4] = "O"
    elif wrongGuessCount == 3:
        board[3] = "/"
    elif wrongGuessCount == 4:
        board[5] = "\\"
    else:
        board[7] = "O"


main()
