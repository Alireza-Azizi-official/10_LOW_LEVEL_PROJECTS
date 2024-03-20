import random
from artt import vs
import instaloader
import time

L = instaloader.Instaloader()
user_list = ['nasa', 'cristiano', 'leomessi', 'ufc', 'mmafighting', 'lovethenature95']
data_dict = {user: 0 for user in user_list}

for user in user_list:
    profile = instaloader.Profile.from_username(L.context, user)
    data_dict[user] = profile.followers


playing=True

while playing:
    point_P = 0
    point_N = 0
    chances = 3
    while point_P < 3 and point_N < 3 and chances > 0:
        
        rand_users = random.sample(list(data_dict.keys()), k=2)

        max_followers_user = ""
        max_followers = 0

        for user in rand_users:
            if data_dict[user] > max_followers:
                max_followers_user = user
                max_followers = data_dict[user]
                
        print("__________________________________________")        
        print("\n"+rand_users[0])
        print(vs)
        print(rand_users[1]+"\n")        
            
        player=input("enter your guess:")

        if player not in user_list:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("you must enter the profile name.")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            
        else:
            
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


                
            else:
                time.sleep(2)
                print("______________")
                print("OOPS.")
                print("______________")
                print(f"the user with the most followers is <<{max_followers_user.upper()}>> with <<{max_followers}>> followers.")
                point_N+=1
                chances -= 1
                print("!! you have:",chances-1, "more chances.")
                

        if point_P == 3:
            time.sleep(1)
            print("YOU ARE GOD OF THIS GAME.\n")
            break
        elif point_N == 3:
            print("YOU LOSE THE GAME.")
            print(f"the user with the most followers is <<{max_followers_user.upper()}>> with <<{max_followers}>> followers.")
            break

        if chances ==0:
            print("you lose the game you have 0 chanses to guess")
            break

    restart = input("Do you want to restart the game? (Y/N) ").lower()
    if restart != "y":
        print("Thanks for playing!")
        break
        