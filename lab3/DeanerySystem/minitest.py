import unittest
from term import Term
from day import Day


class Test_Term(unittest.TestCase):
    term1 = Term(Day.TUE, 9, 45)
    term2 = Term(Day.WED, 10, 15)

    def test_stringify(self):
        print(self.term1, self.term2)

    def test_earlier(self):
        self.assertEqual(self.term1.earlierThan(self.term2), True)

    def test_later(self):
        self.assertEqual(self.term1.laterThan(self.term2), False)

    def test_equals(self):
        self.assertEqual(self.term1.equals(self.term2), False)


if __name__ == '__main__':
    unittest.main()
