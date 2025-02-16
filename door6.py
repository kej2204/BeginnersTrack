import random
def door6():
    print("For door 6, you will risk it all. Each time you see the word 'bet,' you can choose whether to bet or not.")
    print("If you bet, you may lose or gain points in order to win. If you don't bet, your number of points won't change.")
    print("You have 5 bets to gain at least 12 points. Losing the game results in losing 1 life.")

    points = 0
    tries = 0
    while tries < 5:
        print('You currently have {} points. You have {} tries left to reach 12 points.'.format(points, 5-tries))
        user_input = input("Bet? (y/n): ")
        if user_input == 'y':
            points += random.randint(-10,10)
        else:
            print()
        tries+=1
    if points >= 12:
        print("You win!")
        return +1
    else:
        print("Boo. You lose.")
        return -1
    
door6()
    