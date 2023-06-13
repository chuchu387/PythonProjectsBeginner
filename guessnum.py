import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    attemps = 0
    while guess != random_number:
        guess = int(input(f"Guess a number betwen 1 and {x}"))
        print(guess)
        if guess < random_number:
            print("Sorry, guess again, too low")
        elif guess > random_number:
            print("Sorry, guess again, too high")
    print(f"yay congrats, you have guessed a random number succesfully in {attemps}!")
    
guess(100)

# import random

# def guess_number():
#     print("Welcome to the Number Guessing Game!")
#     print("Think of a number between 1 and 100.")
    
#     low = 1
#     high = 100
#     attempts = 0
    
#     while True:
#         guess = random.randint(low, high)
#         print(f"The computer guesses: {guess}")
        
#         response = input("Is the guess correct (C), too low (L), or too high (H)? ").upper()
        
#         if response == "C":
#             print(f"The computer guessed your number in {attempts} attempts!")
#             break
#         elif response == "L":
#             low = guess + 1
#         elif response == "H":
#             high = guess - 1
#         else:
#             print("Invalid input. Please enter 'C' for correct, 'L' for too low, or 'H' for too high.")
        
#         attempts += 1

# guess_number()
