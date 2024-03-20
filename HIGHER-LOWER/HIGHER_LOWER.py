import random
from artt import logo
from artt import vs
import instaloader


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
print(f"the user with the most followers is <<{max_followers_user.upper()}>> with <<{max_followers}>> followers.")
