import regex
import unittest


class test(unittest.TestCase):
    def test_words(self):
        self.assertEqual(regex.get_parts('Honda rdzewieje szybciej od golfa a to już wyczyn'), {'words': [
                         'Honda', 'rdzewieje', 'szybciej', 'od', 'golfa', 'a', 'to', 'już', 'wyczyn'], 'numbers': []})

    def test_numbers(self):
        self.assertEqual(regex.get_parts('12313 1234 554577 7'), {
                         'words': [], 'numbers': ['12313', '1234', '554577', '7']})

    def test_mixed(self):
        self.assertEqual(regex.get_parts('Statystycznie co 3 polak zjada dziennie 13 placków'), {'words': [
                         'Statystycznie', 'co', 'polak', 'zjada', 'dziennie', 'placków'], 'numbers': ['3', '13']})


unittest.main()
