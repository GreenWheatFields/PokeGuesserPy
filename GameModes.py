import PokeStats

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


def medium_mode(select):
    global total_shown, one
    one = 1
    while one < 2:
        if len(select) == 0:
            print("out of poke")
            break
        poke = PokeStats.Pokemon(29) #select[0]
        select.pop(0)
        poke.printStats()
        print(poke.idnum)
        poke = None
        print("test")
        one +=1


def hard_mode(select):
    global total_shown, one
    one = 1
    print(select)
    while one < 2:
        guess = input("guess a pokemone\n")
        if guess == "lol":
            one += 1
