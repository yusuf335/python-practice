available_exits = ["north", "south", "east", "west"]

chosen_exist = ""

while chosen_exist not in available_exits:
    chosen_exist = input("Please choose a direction:\t").casefold()

    if chosen_exist.casefold() == "quit":
        print("Game over")
        break

else:
    print("Aren't you glad you got out of there")
