empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print(numbers)

for number_lists in numbers:
    print(number_lists)

    for value in number_lists:
        print(value)

# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
# print(numbers)
#
# digits = list("432985617")
# print(digits)
#
# # more_numbers = list(numbers)
# # more_numbers = numbers[:]
# more_numbers = numbers.copy()
# print(more_numbers)
# print(numbers is more_numbers)
# print(numbers == more_numbers)


# print(min(even))
# print(max(even))
#
# print(min(odd))
# print(max(odd))
#
# print()
#
# print(len(even))
# print(len(odd))
#
# print()
# string_count = input("Please enter the alphabet you want to count in mississippi:\t")
# print("mississippi".count(string_count))
