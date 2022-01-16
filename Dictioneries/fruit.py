fruit = {"orange": "asweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a spur, green citrus fruit"}

print(fruit)
print()

veg ={"cabbage": "Every child's favourite",
      "sprouts": "mmm, Lovely",
      "spinach": "can I have some more"}

print(veg)
print()

veg.update(fruit)
print(veg)
print()

nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)