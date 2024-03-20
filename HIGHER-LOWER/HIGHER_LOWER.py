import random
from artt import vs
import instaloader
import time
import clear

# finding the number of followers of instagram accounts.
L = instaloader.Instaloader()
user_list = ['nasa', 'cristiano', 'leomessi', 'ufc', 'mmafighting', 'lovethenature95']
# put them in a dict to call them later.
data_dict = {user: 0 for user in user_list}

for user in user_list:
    profile = instaloader.Profile.from_username(L.context, user)
    data_dict[user] = profile.followers

# making a loop to play the game.
playing=True

while playing:
    # positive/negative point to count the ponits and remained chance to guess.
    point_P = 0
    point_N = 0
    chances = 3
    # make a condition to continue the game.
    while point_P < 3 and point_N < 3 and chances > 0:
        time.sleep(3)
        clear.clear()
        
        # choose 2 random user from the converted dict to list.
        rand_users = random.sample(list(data_dict.keys()), k=2)

        max_followers_user = ""
        max_followers = 0
        # find the user with most followers.
        for user in rand_users:
            if data_dict[user] > max_followers:
                max_followers_user = user
                max_followers = data_dict[user]
                
        print("__________________________________________")        
        print("\n"+rand_users[0])
        print(vs)
        print(rand_users[1]+"\n")        
        # take input from the player.  
        player=input("enter your guess:")
        # raise error in case the player entered incorrectly.
        if player not in user_list:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("you must enter the profile name.")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            
            
        else:
            # if the guess was correct add to the positive point and put chances -1.
            if player == max_followers_user:
                time.sleep(2)
                print("++++++++++++++++++++++++")
                print("WOW YOU GUESS CORRECTLY.")
                print("++++++++++++++++++++++++")
                print(f"the user with the most followers is <<{max_followers_user.upper()}>> with <<{max_followers}>> followers.")
                point_P+=1
                print("you have",point_P,"points.")
                chances -= 1
                print("!! you have:",chances-1, "more chances.")
                


            #  if the guess was incorrect add to the negative point and put chances -1.   
            else:
                time.sleep(2)
                print("______________")
                print("OOPS.")
                print("______________")
                print(f"the user with the most followers is <<{max_followers_user.upper()}>> with <<{max_followers}>> followers.")
                point_N+=1
                chances -= 1
                print("!! you have:",chances-1, "more chances.")
                
                
        # if positive point was equal to  3 then quit the game and print you win.
        if point_P == 3:
            time.sleep(1)
            print("YOU ARE GOD OF THIS GAME.\n")
            break
        # if negative point was equal to 3 then quit the game and print you loose.
        elif point_N == 3:
            print("YOU LOOSE THE GAME.")
            print(f"the user with the most followers is <<{max_followers_user.upper()}>> with <<{max_followers}>> followers.")
            break
        # if chances was equal to 0 then print you loose the game and quit.    
        if chances ==0:
            print("you loose the game you have 0 chanses to guess")
            break
    # ask the user if he want's to replay.if yes continue if not print thanks and quit the game.       
    restart = input("Do you want to restart the game? (Y/N) ").lower()
    if restart != "y":
        clear.clear()
        print("Thanks for playing!")
        break
        