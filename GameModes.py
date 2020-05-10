total_shown, one = 0, 1


def easy_mode(select):
    global total_shown, one
    one = 1
    print(select)
    while one < 2:
        guess = input("guess a pokemone\n")
        if guess == "lol":
            one += 1

    print("correct")
