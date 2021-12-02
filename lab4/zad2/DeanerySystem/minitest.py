import unittest
from term import Term
from day import Day
from lesson import Lesson


class Test_Term(unittest.TestCase):
    term1 = Term(9, 45, 90, Day.TUE)
    term2 = Term(10, 15, 90, Day.WED)

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

    def test_lesson_create(self):
        lesson = Lesson(Term(9, 35, 90, Day.TUE),
                        "Programowanie skryptowe", "Stanisław Polak", 2)

        self.assertEqual(str(lesson),
                         """Programowanie skryptowe (Wtorek 9:35-11:05)\n2 rok studiów stacjonarnych\nProwadzący: Stanisław Polak""")

    def test_lesson_earlier_day_success(self):
        lesson = Lesson(Term(9, 35, 90, Day.TUE),
                        "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson.earlierDay()

        self.assertEqual(str(lesson),
                         """Programowanie skryptowe (Poniedziałek 9:35-11:05)\n2 rok studiów stacjonarnych\nProwadzący: Stanisław Polak""")

    def test_lesson_earlier_day_fail(self):
        lesson = Lesson(Term(19, 35, 90, Day.FRI),
                        "Programowanie skryptowe", "Stanisław Polak", 2)
        self.assertEqual(str(lesson),
                         """Programowanie skryptowe (Piątek 19:35-21:05)\n2 rok studiów niestacjonarnych\nProwadzący: Stanisław Polak""")
        lesson.earlierDay()
        self.assertEqual(str(lesson),
                         """Programowanie skryptowe (Piątek 19:35-21:05)\n2 rok studiów niestacjonarnych\nProwadzący: Stanisław Polak""")

    def test_lesson_later_day_success(self):
        lesson = Lesson(Term(9, 35, 90, Day.TUE),
                        "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson.laterDay()

        self.assertEqual(str(lesson),
                         """Programowanie skryptowe (Środa 9:35-11:05)\n2 rok studiów stacjonarnych\nProwadzący: Stanisław Polak""")

    def test_lesson_later_day_fail(self):
        lesson = Lesson(Term(12, 35, 90, Day.FRI),
                        "Programowanie skryptowe", "Stanisław Polak", 2)
        self.assertEqual(str(lesson),
                         """Programowanie skryptowe (Piątek 12:35-14:05)\n2 rok studiów stacjonarnych\nProwadzący: Stanisław Polak""")
        lesson.laterDay()
        self.assertEqual(str(lesson),
                         """Programowanie skryptowe (Piątek 12:35-14:05)\n2 rok studiów stacjonarnych\nProwadzący: Stanisław Polak""")

    def test_lesson_later_time_success(self):
        lesson = Lesson(Term(9, 30, 90, Day.TUE),
                        "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson.laterTime()

        self.assertEqual(str(lesson),
                         """Programowanie skryptowe (Wtorek 11:00-12:30)\n2 rok studiów stacjonarnych\nProwadzący: Stanisław Polak""")

    def test_lesson_later_time_fail(self):
        lesson = Lesson(Term(16, 00, 60, Day.FRI),
                        "Programowanie skryptowe", "Stanisław Polak", 2)
        self.assertEqual(str(lesson),
                         """Programowanie skryptowe (Piątek 16:00-17:00)\n2 rok studiów stacjonarnych\nProwadzący: Stanisław Polak""")
        lesson.laterTime()
        self.assertEqual(str(lesson),
                         """Programowanie skryptowe (Piątek 16:00-17:00)\n2 rok studiów stacjonarnych\nProwadzący: Stanisław Polak""")

    def test_lesson_earlier_time_success(self):
        lesson = Lesson(Term(9, 30, 90, Day.TUE),
                        "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson.earlierTime()

        self.assertEqual(str(lesson),
                         """Programowanie skryptowe (Wtorek 8:00-9:30)\n2 rok studiów stacjonarnych\nProwadzący: Stanisław Polak""")

    def test_lesson_earlier_time_fail(self):
        lesson = Lesson(Term(17, 00, 60, Day.FRI),
                        "Programowanie skryptowe", "Stanisław Polak", 2)
        self.assertEqual(str(lesson),
                         """Programowanie skryptowe (Piątek 17:00-18:00)\n2 rok studiów niestacjonarnych\nProwadzący: Stanisław Polak""")
        lesson.earlierTime()
        self.assertEqual(str(lesson),
                         """Programowanie skryptowe (Piątek 17:00-18:00)\n2 rok studiów niestacjonarnych\nProwadzący: Stanisław Polak""")


if __name__ == '__main__':
    unittest.main()
