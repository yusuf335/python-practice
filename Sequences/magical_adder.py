numbers = input('Please enter Three numbers separated by comma ",":')

split_numbers = numbers.split(",")

print(split_numbers)

int_token = []
for st in split_numbers:
    int_token.append(int(st))
print(st)

a, b, c = int_token
result = a + b - c
print(result)
