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

    def test_changeTerm(self):
        term1 = Term(Day.TUE, 9, 45)
        self.assertEqual(term1.setTerm(
            "27 X 2021 8:00 - 27 X 2021 8:30"), True)
        self.assertEqual(str(term1), "Środa 8:00 [30]")
        self.assertEqual(term1.setTerm(
            "29 XI 2021 8:00 - 27 X 2022 9:30"), True)
        self.assertEqual(str(term1), "Poniedziałek 8:00 [478170]")


if __name__ == '__main__':
    unittest.main()
