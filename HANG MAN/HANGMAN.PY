import random 
from  collections import Counter
import time

words = ["Porsche","Polestar","Tesla","Subaru","Alfa_Romeo","Kia","Mazda","Lexus" ]
word=random.choice(words)
chances=len(word)-1
repeatedletter=''
if __name__=='__main__':
    print("Hello dear player, guess the word:")
    print(f'HINT : It\'s name of a car.')
    print(f'You have {chances} chances.')
    guess = list(word)  
    guess[0] = word[0]  
    for i in range(1, len(word)):
        guess[i] = '_'  
    print(' '.join(guess))
    
    print("Get ready...")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    print("Go!")
    
    input("Press any key to start...")
    
    while (chances != 0):
        chances-=1
        try:
            player=str(input("\nPlease enter a character: ")).lower()
        except:
            print('Please enter only one letter at a time.')
            continue
        if not player.isalpha():
            print('!!You can only enter alphabet not number!!')
        elif len(player)>1:
            print(f"Pay attention : you must enter only one letter at the same time.you only have {chances}")
        elif player in repeatedletter:
            print("you said that, guess another letter.")
        else:
            if player in word:
                a=word.count(player)
                for _ in range(a):
                    repeatedletter += player
                for i, char in enumerate(word):
                    if char == player:
                        guess[i] = char
            print(' '.join(guess))
            print(f'you have {chances+1} more chances.')
            if Counter(guess) == Counter(word):
                print(f'You win! The word is {word}.')
                break    
        repeatedletter += player

    if chances == 0 :
        print('\nYou have no more chances.\nYou loose.')
        print(f'The word was :{word}.')