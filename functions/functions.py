def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text


# with open("centred", mode='w') as centre_file:
# s1 = centre_text("Spam and Eggs")
# print(s1)
# print(centre_text("Spam, spam and Eggs"))
# print(centre_text(12))
# print(centre_text("spam, spam, spam and spam"))
# print(centre_text("first", "second", 3, 4, "spam", sep=':'))

with open("menu", "w") as menu:
    s1 = centre_text("Spam and Eggs")
    print(s1, file=menu)
    print(centre_text("Spam, spam and Eggs"))
    print(centre_text(12))
    print(centre_text("spam, spam, spam and spam"))
    print(centre_text("first", "second", 3, 4, "spam", sep=':'))
