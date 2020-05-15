import PokeStats

total_shown, one = 0, 1


def easy_mode(select, mode):
    global total_shown, one
    one = 1
    print(select)
    while one < 2:
        guess = input("guess a pokemone\n")
        if guess == "lol":
            one += 1

    print("correct")


def medium_mode(select, mode):
    global total_shown, one
    one = 1
    three = 3
    while one < 2:
        if len(select) == 0:
            print("out of poke")
            break
        poke = PokeStats.Pokemon(select[0], mode) # select[0]
        select.pop(0)
        print(poke.name)
        print(poke.idnum)
        print("test")
        guess = input("Guess a Pokemon\n")
        while three < 4:
            if guess.lower() == poke.name.lower():
                print("correct generating new poke")
                medium_mode(select, mode)
                three += 1
            elif guess.lower() != poke.name.lower():
                print("wrong")
                guess = input("Guess a Pokemon\n")

        one +=1
        poke = None

def hard_mode(select):
    global total_shown, one
    one = 1
    print(select)
    while one < 2:
        guess = input("guess a pokemone\n")
        if guess == "lol":
            one += 1
