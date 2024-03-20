import instaloader
L = instaloader.Instaloader()
user_list=['nasa','cristiano','leomessi','ufc','mmafighting','lovethenature95']
followers=[]
for user in user_list:
    profile = instaloader.Profile.from_username(L.context,user)
    followers.append(profile.followers)

a = {user: i for user, i in zip(user_list, followers)}
print(a.keys())

