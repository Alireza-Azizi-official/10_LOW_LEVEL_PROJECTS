# ----------------<<ROCK, PAPER, SCISSORS>--------------------
import random
import time


# to count the points.
player_counts=0
system_counts=0

# player part.
while True:
    print('<<----------------------------------------->>')
    print(" 1= rock \n 2= paper \n 3= scissors \n")
    
    player=int(input("please enter your choice: \n"))
    
    while player>3 or player<1:
        player=int(input('you only can enter one number between 1 to 3: \n'))
    
    if player==1:
        print('player_1 = rock')
        
    elif player==2:
        print('player_2 = paper')
        
    else:
        print('player_3 = scissor')
        
            
    # system part.
    system=random.randint(1,3)
    if system==1:
        print('system_1 = rock')
    elif system==2:
        print('system_2 = paper')
    else:
        print('system_3 = scissor')
        
    
    

    # add timer to have a little bit delay in the game.
    time.sleep(2)
    
    # game conditions.
    if player == system:
        print('DRAW') 
        print('your point:',player_counts, 'system point:', system_counts )
        
    elif player==1 and system==2:
        print('YOU LOOS \n')
        system_counts+=1
        print('your point:',player_counts, 'system point:', system_counts )
        
    elif player==1 and system==3:
        print('YOU WIN \n')
        player_counts+=1 
        print('your point:',player_counts, 'system point:', system_counts )
               
    elif player==2 and system==1:
        print('YOU WIN \n')
        player_counts+=1        
        print('your point:',player_counts, 'system point:', system_counts )
        
    elif player==2 and system ==3:
        print('YOU LOOS \n')
        system_counts+=1
        print('your point:',player_counts, 'system point:', system_counts )

    elif player==3 and system==1:
        print('YOU LOOS \n')
        system_counts+=1
        print('your point:',player_counts, 'system point:', system_counts )

    elif player==3 and system==2:
        print('YOU WIN \n')
        player_counts+=1        
        print('your point:',player_counts, 'system point:', system_counts )
     
    # to check the points if any side reaches to 3 point firt then that part is the player.
    if player_counts == 3 or system_counts == 3 :
        if player_counts > system_counts:
            print('*_*_*_*_*_*_*_*_*_*_*_*_*')
            print('WOW YOU ARE THE WINNRE.') 
            print('*_*_*_*_*_*_*_*_*_*_*_*_*') 
            break 
        else:
            print('!_!_!_!_!_!_!_!_!')
            print('OOPS YOU LOOSE.')
            print('!_!_!_!_!_!_!_!_!')
            break
        
    
    
   

