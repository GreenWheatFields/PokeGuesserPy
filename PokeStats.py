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
        self.type1 = self.stats["types"][1]["type"]["name"]

    def printPoke(self):
        print(self.idnum)

    def printStats(self):
        print(self.type1)
        print(len(self.stats["types"]))
