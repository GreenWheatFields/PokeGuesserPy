import requests as r
import json
from bs4 import BeautifulSoup


class Pokemon:

    def __init__(self, randomPoke):
        self.idnum = randomPoke
        self.stats = json.loads(r.get("https://pokeapi.co/api/v2/pokemon/" + str(self.idnum)).text)
        self.name = self.stats["name"].capitalize()
        self.heightInFeet = int(self.stats["height"] / 3.048)  # decimeteres
        self.weightInLbs = int(self.stats["weight"] / 4.536)  #
        self.baseExp = self.stats["base_experience"]
        self.type1, self.is2Types, self.type2 = Pokemon.getTypes(self)
        self.firstGens = Pokemon.getFirstGens(self)
        self.frontSprite = self.stats["sprites"]["front_default"]
        '''parse bulbapedia'''
        # check name for exceptions
        self.name, self.parseKey = Pokemon.checkName(self)

    def printStats(self):
        pass

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
        genSelect = len(self.stats["game_indices"])  # gen the last gen listed, which is the first appearance
        # PokeApi doesnt have generations for id's after 649
        if 650 <= self.idnum <= 721:
            self.firstGens = "X and Y"
        elif 722 <= self.idnum <= 807:
            self.firstGens = "Sun and Moon"
        else:
            self.firstGens = self.stats["game_indices"][genSelect - 1]["version"]["name"].capitalize() + " and " + \
                             self.stats["game_indices"][genSelect - 2]["version"]["name"].capitalize()
        return self.firstGens

    def checkName(self):

        if self.name == "Nidoran-f":
            self.name = "Nidoran♀"
            self.parseKey = "Nidoran♀"
        elif self.name == "Farfetchd":
            self.

        return self.name, self.parseKey
