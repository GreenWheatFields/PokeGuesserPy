import unittest
from PokeStats import Pokemon
from bs4 import BeautifulSoup
import time


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.select = list(range(0, 808))
        self.count = 0

    def test_checkImages(self):
        # checking to see if the links are empty
        for i in self.select:
            poke = Pokemon(self.select[0], "medium")
            self.select.pop(0)

            self.count += 1
            self.assertGreater(len(poke.bulbapedia.find_all("img", width="250")), 0)



if __name__ == '__main__':
    unittest.main()
