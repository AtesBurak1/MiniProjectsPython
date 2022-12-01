import random
import string
from words import mylist

def get_valid_word(mylist):
    global word
    word = random.choice(mylist) #rastgele bir seçim
    while ' ' in word or '-' in word:
        word = random.choice(mylist)
        
        
        
    return word


def hangman():
    word = get_valid_word(mylist).upper()
    word_letters = set(word) # kelimedeki harfleri alma
    alphabet = set(string.ascii_uppercase) # Ascii table büyük harfler
    used_letters = set() # kullanılan harfler
    lives = 10
    while len(word_letters) > 0 and lives > 0:
        print("Letters are used:", ' '.join(used_letters)) #kullanılan
        

           #kelime(A - - - K) şeklinde
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(f"You have {lives} lives. Current word is:", ' '.join(word_list))
        
        
        user_letter= input("Input a letter: ").upper()
        # kullanıcıdan alın harfin alfabede olması ve ya daha önce kullanışmış olma durumları
        if user_letter in alphabet - used_letters :
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
        elif user_letter in used_letters:
             print('You have already used that letter before. Try an another one.')
        else:
            print('Invalid Charahter!') 
        if len(word_letters) == 0:
              print('You are awesome! You get the word:', word,) 
        elif lives == 0:
            print('You lost dude!')      

print(mylist[2])
#hangman()

