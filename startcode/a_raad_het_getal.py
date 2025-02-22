import random

def is_number_guessed(guess, secret_number):
    if guess == secret_number:
        print("yippie :D")
        return True

    else:
        print("womp womp")
        return False

def guess_the_number(big):
    secret_number = random.randint(1, big)
    end_game = False
    while not end_game:
        guess = int(input("give number"))
        guessed = is_number_guessed(guess, secret_number)
        if guessed == True:
            end_game = True

guess_the_number(5)
