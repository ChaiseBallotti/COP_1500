#inclass
import random

#for i in range(10):
    #x = random.randint(1,10)
    #y = random.randint(1,10)
    #print(x+y)
    #print(x)
    #print(y)
    #print(random.randint(1,10))

num = random.randint(1,100)
print(num)

def user() -> int:
    """prompts the user for a guess and returns users guess"""
    while True:
        #get int from user
        guess = int(input("""Guess an interger between 1 and 100, inclusive: """))
        if guess <= 100 and guess >= 0:

            break
        else:
            print("Not a valid number")
    return guess

g = 0
while num != g:
    g = user()

    if num == g:
        print("Winner winner chicken dinner")
        print(n)
    elif num > g:
        print("Your guess is too low")
    else:
        print("your guess is too high")
"""keep track of how many guesses, and return that value"""