import requests as r
import json
import lxml
import textwrap
from bs4 import BeautifulSoup


class Pokemon:

    def __init__(self, randomPoke, mode):
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
        self.name, self.parseKey, self.urlName = Pokemon.checkName(self)
        bulbapedia = BeautifulSoup(r.get("https://bulbapedia.bulbagarden.net/wiki/" + self.urlName + "_(Pokémon)").text,
                                   features="lxml")
        self.desc = Pokemon.getDesc(self, bulbapedia, mode)

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
            self.name = "Nidoran f"
            self.parseKey = self.urlName = "Nidoran♀"
        elif self.name == "Farfetchd":
            self.name = self.parseKey = "Farfetched'd"
            self.urlName = "Farfetch%27d"
        elif self.name == "Mr-mime":
            self.name = self.parseKey = "Mr. Mime"
            self.urlName = "Mr._Mime"
        elif self.name == "Mime-jr":
            self.name = self.parseKey = "Mime Jr."
            self.urlName = "Mime_Jr."
        elif self.name == "Meloetta-aria":
            self.name = self.parseKey = self.urlName = "Meloetta"
        elif self.name == "Type-null":
            self.name = self.parseKey = "Type: Null"
            self.urlName = "Type:_Null"
        elif "Tapu-" in self.name:
            self.name = self.name.replace("-", " ")
            self.name = self.parseKey = self.name[:5].capitalize() + self.name[5:].capitalize()
            self.urlName = self.name.replace(" ", "_")
        else:
            self.parseKey = self.urlName = self.name

        return self.name, self.parseKey, self.urlName

    def getDesc(self, bulbapedia, mode):
        print(bulbapedia.select_one("#mw-content-text > p:nth-child(3)").text)

        parseText = 3
        self.desc = ""
        if mode == "easy":
            while parseText <= 8:
                try:
                    self.desc += bulbapedia.select_one("#mw-content-text > p:nth-child(" + str(parseText) + ")").text.replace(self.parseKey, "_____")
                except AttributeError:
                    pass
                parseText += 1
        #print("final")
        wrapper = textwrap.TextWrapper(width=75)
        self.desc = wrapper.fill(text=self.desc)
        print(self.desc)
        return self.desc
