fruit = {"orange": "asweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a spur, green citrus fruit"}

# print(fruit)
# print(fruit["lemon"])
#
# fruit["pear"] = "an add shaped aple"
# print(fruit)
# del fruit["lemon"]
# print(fruit)

# print(fruit)
# while True:
#     dict_key = input("Please enter fruit:")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("we don't have a" + dict_key)

# for f in sorted(fruit.keys()):
#     print(f + "-" + fruit[f])

# for f in fruit:
#     print(f + "-" + fruit[f])

# for val in fruit.values():
#     print(val)

# fruit_keys = fruit.keys()
# print(fruit_keys)

print(fruit.items())

print()
f_tuple = tuple(fruit.items())
print(f_tuple)

print()
for snack in f_tuple:
    item, description = snack
    print(item + "is" + description)