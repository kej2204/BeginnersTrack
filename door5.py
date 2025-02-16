def door5():
    user_guess = input("For this door, you will have unlimited attempts to guess the secret word formed by the given letters. The letters are: 'a,' 'o,' 's,' 'c,' and 't.' Each of the five letters is used just once in the secret word. Enter your answer here: ").lower()
    while user_guess != 'ascot' and user_guess != 'coast' and user_guess != 'tacos' and user_guess != 'coats':
        print("Incorrect guess!")
        user_guess = input("Try again here: ")
    print("Correct! The secret word was {}.".format(user_guess))
    return +1

        