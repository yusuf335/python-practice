import random


def get_integer(prompt):
    """
    Get an interger from standard Input (stdin).

    The function will continue looping and prompting
    the user, untl a valid `int` is entered.

    :param prompt: The String that the user will see, when
        they're promoted to eneter the value.
    :return:The integrer that the user eneters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("Enter valid integer")


highest = 1000
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing
guess = 0

print("Please guess a number 1 to {}:".format(highest))
guess = get_integer(": ")

if guess == answer:
    print("You got it first time")
else:
    while guess != answer :
        if guess < answer:
            print("Please guess higher or To quit the game enter 0")
        else: # guess must be greater than answer
            print("Please guess lower or To quit the game enter 0")
        guess = get_integer(": ")
        if guess == answer:
            print("Well done, you gussed it")
            break
        if guess == 0:
            print("Try next time")
            break



