import random
from artt import logo
from artt import vs
import instaloader



def data():
    L = instaloader.Instaloader()
    user_list=['nasa','cristiano','leomessi','ufc','mmafighting','lovethenature95']
    followers=[]
    for user in user_list:
        profile = instaloader.Profile.from_username(L.context,user)
        followers.append(profile.followers)
    return followers

def data_func():
    return data()

def assign():
    return random.choice(data_func())


def logic(user1, user2, guess, max):

    final_user = {user1, user2}

    for _ in final_user:
        if user1 > user2:
            max += str(user1)
        else:
            max += str(user2)

    if max == guess:
        return True, max
    else:
        return False, max

def play():
    play = True

    while play:
        point = 0
        game_running = True

        while game_running:
            print(logo)
            a = assign()
            b = assign()

            if point > 0:
                a = b
                b = assign()

                if a == b:
                    b = assign()

            print(a)
            print(vs)
            print(b)

            print("__________________________")
            print(f"YOU HAVE {point} POINTS.")
            print("__________________________")

            guess = input("enter your guess:")

            if logic(a, b, guess, max):
                point += 1
                max = max_guess
            else:
                game_running = False

        restart = input("I DON'T SUGGEST BUT DO YOU WANT TO RESTART?(Y/N)").lower()

        if restart == 'y':
            max_guess = ""
            guess = input("enter your guess:")
        elif restart =='n':
            print("so what are you doing here?")
        else:
            print("if you can't even enter one of two letters then you'd better not to play.")

play()