import random

#take the players name.
name=str(input("what's your name?"))

#create a loop to restart the game if the player wants.
while True:
    guesses=''
    #number of times that you can guess
    turns=4
    print("good luck",name,"you have:",turns, "turns.")
    words=['rainbow', 'computer', 'science', 'programming','python', 'mathematics', 'player', 'condition','reverse', 'water', 'board', 'geeks']
    
    #choose a word from the list randomly.
    word=random.choice(words)
    
    #take the players guess.
    print("guess the charecter:")
    
    #check if the entered alphabet is in the word or not.if it wasn't correct then your turns would be reduced.
    while turns > 0 :
        failed=0
        for alpha in word:
            if alpha in guesses:
                print(alpha,end=" ")
            else:
                print("_")
                failed+=1
        if failed == 0 :
            print("you are a clever person. you win")
            print("\n the word is: ", word)
            
        else:
            print()
            guess=str(input("enter another charecter:"))
            guesses += guess
            
        if guess not in word:
            turns -= 1
            print('you are idiot')
            print("\n you only have :",turns,"more turns.")
        
        #if your turns are 0 then you will lose and the game is finished.
        if turns == 0 :
            print("your IQ is less than a red fish go and kill yourself like a dog.")
            break
        
    #to see if the player wants to play again.
    restart_game=str(input("if you lose I don't suggest to restart otherwise enter 'r' to play again:"))
    if restart_game != "r" and restart_game !="R":
        break
    