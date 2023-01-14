import unittest
from translator import englishtofrench, frenchtoenglish

class TestTranslateFunctions(unittest.TestCase):
    def test_nul(self):
        self.assertEqual(englishtofrench(None), None)
        self.assertEqual(frenchtoenglish(None), None)


    def test_space(self):
        self.assertEqual(englishtofrench(' '), ' ')
        self.assertEqual(frenchtoenglish(' '), ' ')


    def test_hello(self):
        self.assertEqual(englishtofrench('Hello'), 'Bonjour')
        self.assertEqual(frenchtoenglish('Bonjour'),'Hello' )

    def test_new_line(self):
        self.assertEqual(englishtofrench(
            "I'm tired today.\nHello"),
            "Je suis fatigué aujourd'hui.\nBonjour"
        )
        self.assertEqual(frenchtoenglish(
            "Je suis fatigué aujourd'hui.\nBonjour"),
            "I'm tired today.\nHello"
        )

    
    def test_untranslatable(self):
        self.assertEqual(englishtofrench(
            "Глупый тест"),
            "Глупый тест"
        )
        self.assertEqual(frenchtoenglish(
            "Глупый тест"),
            "Глупый тест"
        )


if __name__ == '__main__':
    unittest.main()        