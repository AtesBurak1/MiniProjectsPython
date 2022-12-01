import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors:")
    computer = random.choice(['r','p','s'])
    
    if user == computer:
        print('Tie')
    elif user == 'r':
        if computer == 'p':
            print(" You lost.")
        else:
            print("You win!")
    elif user == 'p':
        if computer == 's':
            print(" You lost.")
        else:
            print("You win!")
    else:
        if computer == 'r':
            print(" You lost.")
        else:
            print("You win!")
            
play()