
option = "-"

while option != "0":

    if option in "12345":
        print("\nYou have choosed option {}".format(option))
    else:
        print("Please choose your option from the list below: \n1. Learn Python "
              "\n2. Learn Java \n3. Go swimming \n4. Have dinner \n5. Go to bed "
              "\n0. Exit")

    option = input("\nEnter your number:\t")



