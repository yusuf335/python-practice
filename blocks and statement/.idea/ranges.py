# for i in range(10, 0, -2):
#     print("i is now {}".format(i))
#
# for i in range(0, 100, 7):
#     print(i)

# Modify the code inside this loop to stop when i is greater than zero and exactly divisible by 11
for i in range(21):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)


