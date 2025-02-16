def door2(): 
    print("Welcome to the trivia minigame. Only enter one-word answers. Answers are not case-sensitive. You must answer 3 questions correctly.")
    questions = ["What is the title of the satirical 1945 novel about farm animals who rebel against their human owner?", "What was the first group of people to use scarecrows?", "True or false: Mother pigs sing to their babies."]
    answers = ["animal farm", "egyptians", "true"]

    success_message = "Correct!"
    fail_message_template = "Boo. That was not correct. The correct answer was: "

    for i in range(len(questions)): # range does not include the value in paranthesis. inclusive on starting but not ending index
        print("\n"+questions[i])
        user_guess = input("Enter your answer here: ").lower()
        if user_guess == answers[i]: #paranthesis for range/length, square brackets for lists
            print(success_message)
        else:
            print(fail_message_template + answers[i])
            return -1
        
    print("\nCongratulations! You passed round 2.")
    return 0

