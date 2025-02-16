from door1 import door1
from door2 import door2
from door3 import door3
from hangman import hangman
from door5 import door5
from door6 import door6
from drawings import oneTurnip, twoTurnips, threeTurnips, oneBarnDoor, twoBarnDoors, threeBarnDoors

lives = 2
play_again = 'y'

print("You have six doors ahead of you. Each contains a peril worse than the next. Choose at your own risk.")
threeBarnDoors()
twoBarnDoors()
oneBarnDoor()
while play_again == 'y' and lives > 0:
    user_input = input("Enter your choice of door (1, 2, 3, 4, 5, or 6) here: ")
    if user_input == '1':
        addition_to_lives = door1()
    elif user_input == '2':
        addition_to_lives = door2()
    elif user_input == '3':
        addition_to_lives = door3()
    elif user_input == '4':
        addition_to_lives = hangman()
    elif user_input == '5':
        addition_to_lives = door5()
    elif user_input == '6':
        addition_to_lives = door6()
    else:
        continue
    lives += addition_to_lives
    print("You have {} lives remaining.".format(lives))
    if(lives >= 3):
        threeTurnips()
    elif(lives == 2):
        twoTurnips()
    elif(lives == 1):
        oneTurnip()
    elif(lives <= 0):
        print("You have run out of lives! You die boo")
        break
    play_again = input("Would you like to try another door? (y/n): ")


   
