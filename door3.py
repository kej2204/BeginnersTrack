from drawings import happyPig, sadPig, confusedPig
import random


def door3():
    win = True
    print("Welcome to the Rock, Hay, Plow door. Rock beats plow, hay beats rock, and plow beats hay.")
    print("Note: this is a bonus round and will not count against you.")
    user_input = input("Enter 1 for rock, 2 for hay, or 3 for plow here: ")
    is_valid_input(user_input)
    comp_choice = random.randint(1,3)

    if comp_choice == 1:
        print("Computer choice is....\nrock")
    elif comp_choice == 2:
        print("Computer choice is....\nhay")
    elif comp_choice == 3:
        print("Computer choice is....\nplow")

    if comp_choice == 1 and user_input == 3:
        print("Rock beats plow. You lose!")
        sadPig()
        win = False
    elif comp_choice == 1 and user_input == 2:
        print("Hay beats rock. You win!")
        happyPig()
        win = True
    elif comp_choice == 2 and user_input == 1:
        print("Hay beats rock. You lose!")
        sadPig()
        win = False
    elif comp_choice == 2 and user_input == 3:
        print("Plow beats hay. You win!")
        happyPig()
        win = True
    elif comp_choice == 3 and user_input == 2:
        print("Plow beats hay. You lose!")
        sadPig()
        win = False
    elif comp_choice == 3 and user_input == 1:
        print("Rock beats plow. You win!")
        happyPig()
        win = True
    elif str(comp_choice) == str(user_input):
        print("DRAW")
        sadPig()
        win = False
    elif(is_valid_input(user_input) == 0):
        sadPig()
        win = False
        return 0
    print("Congratulations! You have completed Door 3.")

    if win == True:
        return +1
    else:
        return 0
    
  

def is_valid_input(user_input):
    if not user_input.isdigit():
        win = False
        print("Invalid input. You lose!.")
        return 0
    
    num = int(user_input)
    return 1 <= num <= 3