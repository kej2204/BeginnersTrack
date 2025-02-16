from door1 import door1

print("You have six doors ahead of you. Each contains a peril worse than the next. Choose at your own risk")
user_input = input("Enter your choice (1, 2, 3, 4, 5, or 6) here: ")

def main():
    lives = 1
    lives += door1()      
    print("You have {} lives remaining.".format(lives))

if user_input == '1':
    main()


   
