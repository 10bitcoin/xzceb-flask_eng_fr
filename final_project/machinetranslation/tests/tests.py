""" Unit Test For Language Translator """
import unittest
from translator import english_to_french 
from translator import french_to_english
class TestAdd(unittest.TestCase):
    """ Test case for Language Translation """
    def test1(self):
        """ French to English & Vice Versa """
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertIsNone(french_to_english(''))
        self.assertIsNone(english_to_french(''))  
if __name__ == '__main__':
    unittest.main()

