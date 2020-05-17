import requests as r
import json
import lxml
from PIL import Image
from io import BytesIO
import textwrap
from bs4 import BeautifulSoup
from decimal import *


class Pokemon:

    def __init__(self, randomPoke, mode):
        self.idnum = randomPoke
        print(self.idnum)
        # for testing
        self.stats = json.loads(r.get("https://pokeapi.co/api/v2/pokemon/" + str(self.idnum)).text)
        self.name = self.stats["name"].capitalize()
        self.heightInFeet, self.weightInLbs = Pokemon.getHeightAndWeight(self)  # decimeteres / #hecograms
        self.baseExp = self.stats["base_experience"]
        self.types = Pokemon.getTypes(self)
        self.firstGens = Pokemon.getFirstGens(self)
        self.frontSprite = self.stats["sprites"]["front_default"]
        '''parse bulbapedia'''
        # check name for exceptions
        self.name, self.parseKey, self.urlName = Pokemon.checkName(self)
        self.bulbapedia = BeautifulSoup(
            r.get("https://bulbapedia.bulbagarden.net/wiki/" + self.urlName + "_(Pokémon)").text, features="lxml")
        self.desc = Pokemon.getDesc(self, mode)
        self.detailedSprite = Pokemon.getDetailedSprite(self)

        ### for tests
        self.picture = None

    def printStats(self):
        pass

    def getTypes(self):
        self.types = self.stats["types"][0]["type"]["name"].capitalize()
        if len(self.stats["types"]) > 1:
            self.types += " and " + self.stats["types"][1]["type"]["name"].capitalize()

        return self.types

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

    def getDesc(self, mode):
        lengths = {"easy": 7, "medium": 6, "hard": 6}
        parseText = 3
        self.desc = ""
        while parseText <= lengths.get(mode):
            try:
                self.desc += self.bulbapedia.select_one(
                    "#mw-content-text > p:nth-child(" + str(parseText) + ")").text.replace(self.parseKey, "_____")
            except AttributeError:
                pass
            parseText += 1
        # print("final")
        wrapper = textwrap.TextWrapper(width=75)
        self.desc = wrapper.fill(text=self.desc)
        self.desc = (self.desc[:350] + '...') if len(self.desc) > 350 else self.desc
        return self.desc

    def getDetailedSprite(self):
        # find all elements with img tag and width=250, the first index of that list is what
        # i want, extract the link with "src"
        return "https:" + self.bulbapedia.find_all("img", width="250")[0]["src"]

    def getHeightAndWeight(self):
        return round(float(self.stats["height"]) / float(3.048)), round(float(self.stats["weight"]) / float(4.536), 2)

    def message(self, mode):
        message = "ID: {}\nHeight: {} ft\nWeight: {} lbs\nFirst Letter: {}\nBase Exp: {}\n".format(self.idnum,
                                                                                                   self.heightInFeet,
                                                                                                   self.weightInLbs,
                                                                                                   self.name[0],
                                                                                                   self.baseExp)
        if mode == "medium" or "easy":
            message += "Type: {}\nFirst Gens: {}\n Description:\n '{}'".format(self.types, self.firstGens, self.desc)

        print(message)
        Pokemon.showImage(self, mode)

    def showImage(self, mode):
        self.picture = None
        print(mode)
        if mode == "easy":
            self.picture = self.detailedSprite
            print("in easy mode")
        elif mode == "medium" or "hard":
            self.picture = self.frontSprite

        image = r.get(self.picture)
        img = Image.open(BytesIO(image.content))
        img.show()
