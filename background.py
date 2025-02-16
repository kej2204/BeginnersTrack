from door1 import door1
from door2 import door2
from door3 import door3
from door5 import door5

lives = 1
play_again = 'y'

print("You have six doors ahead of you. Each contains a peril worse than the next. Choose at your own risk.")

while play_again == 'y' and lives > 0:
    user_input = input("Enter your choice of door (1, 2, 3, 4, 5, or 6) here: ")
    if user_input == '1':
        addition_to_lives = door1()
    elif user_input == '2':
        addition_to_lives = door2()
    elif user_input == '3':
        addition_to_lives = door3()
    elif user_input == '5':
        addition_to_lives = door5()
    else:
        continue
    lives += addition_to_lives
    print("You have {} lives remaining.".format(lives))
    play_again = input("Would you like to try another door? (y/n): ")


   
