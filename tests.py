import unittest
from PokeStats import Pokemon
import PokeStats
from bs4 import BeautifulSoup
import time


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.select = list(range(0, 808))
        self.count = 0
        self.poke = Pokemon(5, "medium")

    def voidtest_checkImages(self):
        # checking to see if the links are empty
        for i in self.select:
            poke = Pokemon(self.select[0], "medium")
            self.select.pop(0)

            self.count += 1
            self.assertGreater(len(poke.bulbapedia.find_all("img", width="250")), 0)

    def voidtest_SpriteDisplay(self):
        poke = Pokemon(2, "easy")
        detailedSprite = poke.detailedSprite
        frontSprite = poke.frontSprite
        poke.showImage("easy")
        self.assertEqual(PokeStats.picture, detailedSprite)
        poke.showImage("medium")
        self.assertEqual(PokeStats.picture, frontSprite)

    def voidtest_names(self):
        try:
            poke = Pokemon(746, "medium")
        except Exception:
            self.fail("Error raised")

    def testCheckImageType(self):
        self.assertTrue(self.poke.getDetailedSprite().endswith(".png"))
        self.assertTrue(self.poke.frontSprite.endswith(".png"))


if __name__ == '__main__':
    unittest.main()
