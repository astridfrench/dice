#Astrid French

import random # we can use function from random library to rolling the dice from 1 - 6
def main():
    print()
    endProgram="no"
    playerOne= "NO NAME"
    playerTwo="No NAME"
    playerOne, playerTwo = inputNames(playerOne, playerTwo)
    while endProgram == 'no': #the loop to run the program
        p1number=0
        p2number = 0
        winnerName = "NO NAME"
        winnerName = rollDice(p1number, p2number, playerOne, playerTwo, winnerName,)
        displayInfo(winnerName)
        endProgram = input('Do you want to end program?(Enter yes or no):') #if the answer is no, it will run the dice again.
        if endProgram == "yes": #if the answer yes, it will print out see you again.
            print("See you again!")
        

def inputNames(playerOne, playerTwo): #to get the player name 1 and 2
    playerOne= input('Enter player 1 name: ')
    playerTwo= input('Enter player 2 name: ')
    return playerOne, playerTwo
    

#this function to ge the roll dice result
def rollDice(p1number, p2number, playerOne, playerTwo, winnerName):
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)
    if p1number == p2number: #if the result same number
        winnerName = "TIE"
    elif p1number>p2number: #if the dice player one is larger than player two
        winnerName=playerOne
    else:
        winnerName=playerTwo #if the dice player two is larger than player one
    return winnerName

#this function to print out the winner
def displayInfo(winnerName):
    print ('The winner is', winnerName)
    

# calls main
main()
