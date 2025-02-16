#pip install wonderwords
from wonderwords import RandomWord


def hangman():

    print("Clover notices the scarecrow is missing! Without it,\nthe pesky crows are feasting on her crops. To rebuild it, \nshe must guess the missing word in Farmer Tom’s old instructions. \nComplete the word before too many wrong guesses or the \nscarecrow stays broken, and Clover loses a turnip.")
    

    r = RandomWord()
    word = r.word(word_min_length=4, word_max_length=4)

    print("\nGuess the word, you have 10 tries before the turnip is gone!")
    guesses = 0
    hiddenWord = '_' * 4

    while guesses < 10:

        guess = input("Enter a letter: ").lower()
        if guess in word:
            print("Correct!")
            hiddenWord = ''.join([guess if word[i] == guess else hiddenWord[i] for i in range(len(word))])
            print(hiddenWord)
            if(hiddenWord == word):
                break
            guesses+=1
        else:
            print("Incorrect!")
            guesses += 1

    if hiddenWord != word:
        print("You lost! The word was: " + word)
        return "fail"
    elif hiddenWord == word:
        print("You won! The word was: " + word)
        return "success"

hangman()