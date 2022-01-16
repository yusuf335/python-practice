number = input("Please enter a series of numbers, using any separators you like:")
separators = ""

for char in number:
    if  char.isnumeric():
        separators = separators + char

print(separators)



