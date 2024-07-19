import random
import math


arr = ['rock', 'paper', 'scissor']

# Função de numero aleatório
def randomNumber():
    number = math.floor(random.random() * len(arr))
    computerChoice = arr[number]
    #print(computerChoice)
    return computerChoice

def startGame():
    try:   
        getComputerChoice = randomNumber()
        print('hello there, welcome to the rock paper and scissor game!\n')
        userChoice = input('please select your choice between:  Rock, Paper and Scissor ') 
    except Exception as e:
        if userChoice != string and userChoice != 'rock' and userChoice != 'paper' and userChoice != 'scissor':
            print('Just String are acceptable, try again')

    
    # draw conditions
    if userChoice == getComputerChoice:
        print(f'thats a draw, you have a {userChoice}')

    elif userChoice == 'rock' and getComputerChoice == 'scissor':
        print(f'Congratulations! you choice {userChoice} and win')

    elif userChoice == 'paper' and getComputerChoice == 'rock':
        print(f'Congratulations! you choice {userChoice} and win')
    
    elif userChoice == 'scissor' and getComputerChoice == 'paper':
        print(f'Congratulations! you choice {userChoice} and win')

    else:
        print('sorry i guess you fail this time.')



startGame()