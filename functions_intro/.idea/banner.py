def banner_text(text: str = "", screen_width: int = 80) ->None:
    if len(text) > screen_width -4:
        raise  ValueError("String {0} is larger then specified width {1}"
                          .format(tex, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)

banner_text("*", 66)
banner_text("""hhhhhhhhhhhhhhhh""", 66)
banner_text(screen_width=50)