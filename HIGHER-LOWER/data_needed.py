import instaloader

def data():
    L = instaloader.Instaloader()
    user_list=['nasa','cristiano','leomessi','ufc','mmafighting','lovethenature95']
    for user in user_list:
        profile = instaloader.Profile.from_username(L.context,user)
        # print(user,"==>", profile.followers)