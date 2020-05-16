import unittest
from PokeStats import Pokemon
from bs4 import BeautifulSoup
import time


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.select = list(range(1, 808))
        self.count = 0

    def test_findBug(self):
        for i in self.select:
            if self.count >= 45:
                time.sleep(45)
            poke = Pokemon(self.select[0], "medium")
            self.select.pop(0)
            print(str(poke.idnum) + " " + poke.name)
            self.count += 1
            self.assertGreater(len(poke.bulbapedia.find_all("img", width="250")), 0)


if __name__ == '__main__':
    unittest.main()
