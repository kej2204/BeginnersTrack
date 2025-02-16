from drawings import happyPig, sadPig, confusedPig
import random


def door3():
    win = True
    print("Welcome to the Rock, Hay, Plow door. Rock beats plow, hay beats rock, and plow beats hay.")
    print("Note: this is a bonus round and will not count against you.")
    user_input = int(input("Enter 1 for rock, 2 for hay, or 3 for plow here: "))
    comp_choice = random.randint(1,3)

    if comp_choice == 1:
        print("Computer choice is....\nrock")
    elif comp_choice == 2:
        print("Computer choice is....\nhay")
    else:
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
    elif comp_choice == user_input:
        print("DRAW")
        sadPig()
        win = False

    print("Congratulations! You have completed Door 3.")

    if win == True:
        return +1
    else:
        return 0
    
  

