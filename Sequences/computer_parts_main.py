from computer_parts_tuples import available_parts

PART_NAME = 0
PART_PRICE = 1

computer_parts = []
cart_price = []

while True:
    print("Computer parts lists")
    for index, (parts_name, parts_price) in enumerate(available_parts):
        print("{0}: {1:<15} BDT {2}".format(index + 1, parts_name, parts_price))

    selected_part = int(input("\nEnter your number:"))
    if 1 <= selected_part <= len(available_parts):
        print("Parts selected: {0} BDT {1}"
              .format(available_parts[selected_part - 1][PART_NAME], available_parts[selected_part - 1][PART_PRICE]))
        chosen_parts = available_parts[selected_part - 1]
        if chosen_parts in computer_parts:
            computer_parts.remove(available_parts[selected_part - 1])
            cart_price.remove((available_parts[selected_part - 1][PART_PRICE]))
        else:
            computer_parts.append(available_parts[selected_part - 1])
            cart_price.append((available_parts[selected_part - 1][PART_PRICE]))
        print("\nParts inside cart:")
        for index, (added_parts, added_parts_price) in enumerate(computer_parts):
            print("{0} {1:<15} BDT {2}"
                  .format(index + 1, added_parts, added_parts_price))
        print("-" * 40)
        total_price = sum(cart_price)
        print("{0:<17} BDT {1}".format("Total price:", total_price))
    else:
        if selected_part > 0:
            print("\nInvalid selection!!! Please select the correct number \n\nTo exit press 0")
        else:
            print("\nYou have exited the program")
            break

    print()
    print("#" * 40)
    print()
