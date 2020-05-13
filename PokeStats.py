import requests as r
import json


class Pokemon:

    def __init__(self, randomPoke):
        self.idnum = randomPoke
        self.stats = json.loads(r.get("https://pokeapi.co/api/v2/pokemon/" + str(self.idnum)).text)
        self.heightInFeet = int(self.stats["height"] / 3.048)  # decimeteres
        self.weightInLbs = int(self.stats["weight"] / 4.536)  #
        self.name = self.stats["name"].capitalize()
        self.baseExp = self.stats["base_experience"]
        self.type1, self.is2Types, self.type2 = Pokemon.getTypes(self)
        self.firstGens = Pokemon.getFirstGens()

    def printStats(self):
        print(len(self.stats["game_indices"]))

    def getTypes(self):
        self.type1 = self.stats["types"][0]["type"]["name"]
        if len(self.stats["types"]) > 1:
            self.is2Types = True
            self.type2 = self.stats["types"][1]["type"]["name"]
        else:
            self.is2Types = False
            self.type2 = None

        return self.type1, self.is2Types, self.type2

    def getFirstGens(self):
        return None