import unittest
from translator import english_to_french
from translator import french_to_english

class testE2F(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(english_to_french(None),"k")
    def test2(self):
        self.assertEqual(english_to_french('Hello'),"Bonjour")
class testF2E(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(french_to_english(None),"k")
    def test2(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")

if __name__== '__main__':
    unittest.main()


