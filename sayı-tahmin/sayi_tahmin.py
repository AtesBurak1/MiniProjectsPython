import random

i=0
guess = 0

random_number = random.randint(1,11)

def random():
    
    global guess
    guess = int(input('Guess the secret number:'))
    
    if(guess == random_number):
        print(' You win!' )
        
    else:
        print('Try again.')
    
   

print('Do you want to play a number guessing game? \n You will have 3 change.')
print(f'{random_number}')

while(guess != random_number):
    random()
    i= i +1
    if guess == random_number:
        break
    elif i>= 3:
        print("Run out of guesses!")
        break

    
        