import random 
from  collections import Counter
import time
#list of different names 
words = ["Porsche","Polestar","Tesla","Subaru","Alfa_Romeo","Kia","Mazda","Lexus" ]
word=random.choice(words)
chances=len(word)-1
repeatedletter = set()
if __name__=='__main__':
    print("Hello dear player, guess the word:")
    print(f'HINT : It\'s name of a car.')
    print(f'You have {chances} chances.')
    guess = ['_'] * len(word)
    guess[0] = word[0]
    print(' '.join(guess))

#add a countdown to think and guess
print("Get ready...")
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)
print("Go!")

input("Press any key to start...")


while (chances != -1):
    start_time = time.time()
    while time.time() - start_time < 3:
        #take an input which is the players guess
        try:
            player=str(input("\nPlease enter a character: ")).lower()
        #to check if the player enterd only one letter
        except:
            print('Please enter only one letter at a time.')
            continue
        #if the player entered more than one letter then break 
        if len(player) > 0:
            break
    #use the countdown to give stress to player!!!
    if len(player) == 0:
        print('You took too long to answer, you lose a chance.')
        continue
    #if the entry wan not alphabet then print an error
    if not player.isalpha():
        print('!!You can only enter alphabet not number!!')
    #if the player entered same letter then raise error
    elif player in repeatedletter:
        print("you said that, guess another letter.")
    #if the letter was correct then put it in the right place and show it
    else:
        if player in word:
            a=word.count(player)
            for _ in range(a):
                repeatedletter.add(player)
            for i, char in enumerate(word):
                if char == player:
                    guess[i] = char
        print(' '.join(guess))
        # count chances and show 
        print(f'you have {chances+1} more chances.')
        if Counter(guess) == Counter(word):
            print(f'You win! The word is {word}.')
            break    
    repeatedletter.add(player)
    # to give stress again!!!
    if len(player)!=0:
        for i in range(3,0,-1):
            print(i)
            time.sleep(0.5)
        print("enter.")
        
        #lose one of the chances if he doesn't enter a letter
        if len(player)==0:
            chances-=1
            print("you lose one of your chances.")
            break
#at last if the chances were equal to 0 then he loses.
if chances == 0 :
    print('\nYou have no more chances.\nYou loose.')
    print(f'The word was :{word}.')