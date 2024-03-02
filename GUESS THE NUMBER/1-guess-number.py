import random
import math

#create a loop to restart the game if the player wants.
while True:
    #take two numbers to choose a number as an answer randomly.
    lower_number=int(input("ENTER A   LOWER NUMBER:"))
    upper_number=int(input("ENTER AN UPPERN NUMBER:"))
    answer=random.randint(lower_number,upper_number)
    
    #count the chances to guess.
    print("YOU HAVE",round(math.log(upper_number - lower_number + 1 ,2)),"CHNACES TO GUESS THE NUMBER.")
    count=0

    while count<round(math.log(upper_number - lower_number + 1,2)):
        #take the guess from player
        count +=1
        player=int(input("ENTER YOUR GUESS PLEASE:"))
        
        #some conditions about guesses and the right answer.if the answer is correct the game will be finished.
        if player==answer:
            print('CONGRATULATION.YOU WIN.YOU DID IT IN',count,'try')
            break
        
        elif player > answer:
            print(f'NO WAY YOUR GUESS IS HIGHER THAN THE ANSWER.')
            
        elif player < answer:
            print(f'OOPS YOUR GUESS IS LESS THAN THE ANSWER.')
    
    #if the player was not able to guess correctly then the text bellow will be shown.        
    if count >=math.log(upper_number - lower_number + 1,2):
        print("YOU ARE A LOOSER. THE CORRECT NUMBER IS",answer)    
        
    #ask if player wants to restart the game by enter 'r' or 'R'.
    play_again=str(input("IF YOU WANT TO PLAY AGAIN ENTER 'R' "))
    if play_again !='r' and play_again !='R':
        break
    
        

    
