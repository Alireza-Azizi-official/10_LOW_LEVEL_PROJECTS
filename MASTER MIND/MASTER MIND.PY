import random

while True:
    number = random.randrange(1000, 2000)
    print(number)
    player = input("enter your guess:")

    if len(player) != 4:
        print("You must enter exactly 4 numbers.")
        continue

    if not all(char.isdigit() for char in player):
        print("You must enter 4 numbers, not any other thing.")
        continue

    player = int(player)
    count=0
    utry = 1
    if number == player and utry==1:
        print("You are a mastermind! You won bro. You win in only", utry, "try.")

    while (number != player):
        utry += 1
        count = 0
        number_str = str(number)
        player_str = str(player)
        correct = ['x'] * 4

        for i in range(0, 4):
            if number_str[i] == player_str[i]:
                count += 1
                correct[i] = number_str[i]
            else:
                continue
        
        print('Not all of them correct but some of them. Try again.')
        print(' '.join(correct))
        player = int(input('Enter your guess:'))
        
    if player == number:
            print("You won bro.")
            print("you can guess in",utry,'try.')
            break
        
