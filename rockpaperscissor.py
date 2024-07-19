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
    print('hello there, welcome to the rock paper and scissor game!\n')
    #Equanto userChoice estiver no arr, não tera problemas
    while True:
        try:   
            userChoice = input('please select your choice between:  Rock, Paper and Scissor ')
            userChoice = userChoice.lower()
            if userChoice not in arr:
                raise ValueError('Please select a valid choice between: Rock, Paper and Scissor')
            break
        except Exception as e: 
            print(f'Unexpected Error {e}')

    getComputerChoice = randomNumber()
    
    # draw conditions
    if userChoice == getComputerChoice:
        print(f'thats a draw, you have a {userChoice}')

    # win conditions
    elif (userChoice == 'rock' and getComputerChoice == 'scissor') or \
         (userChoice == 'paper' and getComputerChoice == 'rock') or \
         (userChoice == 'scissor' and getComputerChoice == 'paper'):
        print(f'Congratulations! You chose {userChoice} and win')


    else:
        print('sorry i guess you fail this time.')

    

startGame()