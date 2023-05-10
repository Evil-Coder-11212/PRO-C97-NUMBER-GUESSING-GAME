import random

while True:
    print("--------------- Guess the number ------------")
    chances = 5
    randomNumber = random.randint(1, 9)
    while chances != 0:
        users_input = input("Enter a guess (between 1 - 10): ")
        users_input_int = int(users_input)
        chances -= 1
        if (users_input_int > randomNumber):
            print("Guess a number lower than ", users_input_int)
        elif users_input_int < randomNumber:
            print("Guess a number higher than ", users_input_int)
        else:
            print("CONGRATULATION YOU WON!!")
            break
    else:
        print("You lost")
