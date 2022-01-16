name = input("Please eneter your name:\t")
age = int(input("Please eneter your age:\t"))

if 18 <= age < 31:
    print("Welcome to club 18-30 holiday, {}".format(name))
else:
    if age < 18:
        print("Sorry, {} you are {} years old need to be above 18".format(name, age))
    else:
        print("Sorry, {} you are {} years old need to be under 31".format(name, age))
