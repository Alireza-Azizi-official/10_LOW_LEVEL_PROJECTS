import random
from artt import logo
from artt import vs
import instaloader
import time

#-------------------------------------------------------------------------------------
#first part
L = instaloader.Instaloader()
user_list=['nasa','cristiano','leomessi','ufc','mmafighting','lovethenature95']
data_dict={
    "nasa": 0,
    "cristiano": 0,
    "leomessi": 0,
    "ufc": 0,
    "mmafighting": 0,
    "lovethenature95": 0,
}

for user in user_list:
    profile = instaloader.Profile.from_username(L.context, user)
    data_dict[user] = profile.followers

rand_users=random.sample(list(data_dict.keys()),k=2)

max_followers_user=""
max_followers=0

for user in rand_users:
    if data_dict[user] > max_followers:
        max_followers_user =user
        max_followers = data_dict[user]

#------------------------------------------------------------------------------------
#second part
print("\n"+rand_users[0])
print(vs)
print(rand_users[1]+"\n")

point_P=0
point_N=0

while point_P + point_N < 3 :
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
            
        else:
            time.sleep(2)
            print("______________")
            print("OOPS.")
            print("______________")
            point_N+=1
            
            
        if point_P== 3 and point_N==0:
            time.sleep(1)
            print("YOU ARE GOD OF THIS GAME.")
            print(f"the user with the most followers is <<{max_followers_user.upper()}>> with <<{max_followers}>> followers.")
            break
        elif point_P > point_N:
            time.sleep(1)
            print("you win")
            break
        else:
            time.sleep(1)
            print("you lose")
            break
time.sleep(2)
print("\n"+rand_users[0])
print(vs)
print(rand_users[1]+"\n")