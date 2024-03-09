import random

while True:
    #generate a 4 digit random number.
    number = random.randrange(1000, 2000)
    #take players guess.
    player = input("enter your guess:")
    #raise error if the player enter less or more than 4 digit.
    if len(player) != 4:
        print("You must enter exactly 4 numbers.")
        continue
    #raise error if the player enter any type than integer.
    if not all(char.isdigit() for char in player):
        print("You must enter 4 numbers, not any other thing.")
        continue

    player = int(player)
    count=0
    #see how many times does the player try.
    utry = 1
    #if the player guess the correct number in just one try then he/she would be the mastermind.
    if number == player and utry==1:
        print("You are a mastermind! You won bro. You win in only", utry, "try.")

    while (number != player):
        utry += 1
        count = 0
        number_str = str(number)
        player_str = str(player)
        correct = ['x'] * 4
        #to check the correct answers of the player and show it.
        for i in range(0, 4):
            if number_str[i] == player_str[i]:
                count += 1
                correct[i] = number_str[i]
            else:
                continue
        #show the right answers
        print('Not all of them correct but some of them. Try again.')
        print(' '.join(correct))
        player = int(input('Enter your guess:'))
    #if the player can guess the right answer in more than one try then this message would return.
    if player == number:
            print("You won bro.")
            print("you can guess in",utry,'try.')
            break
        
