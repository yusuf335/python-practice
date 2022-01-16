import random

highest = 10
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing
guess = 0

print("Please guess a number 1 to {}:".format(highest))
guess =int(input())

if guess == answer:
    print("You got it first time")
else:
    while guess != answer :
        if guess < answer:
            print("Please guess higher or To quit the game enter 0")
        else: # guess must be greater than answer
            print("Please guess lower or To quit the game enter 0")
        guess = int(input())
        if guess == answer:
            print("Well done, you gussed it")
            break
        if guess == 0:
            print("Try next time")
            break



