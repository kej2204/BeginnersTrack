def door1(): 
    print("You must unscramble the word within 3 tries.")
    print("The scrabbled version of the word is: limped")

    answer = "dimple"
    guess = ""
    turn = 0
    max_attempts = 3

    while guess != answer and turn < max_attempts:
        if turn > 0: 
            print("Incorrect answer! Try again")
        guess = input("Please enter your answer here: ").lower()
        turn += 1

    if guess == answer:
        print("Correct! You pass this round")
        return 0
    else: 
        print("You have run out of guesses! You die boo")
        return -1
