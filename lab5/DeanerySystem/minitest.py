from datetime import time
import unittest
from term import Term
from day import Day
from lesson import Lesson
from teacher import Teacher
from timetable1 import Timetable1
from break_module import Break
from timetable2 import Timetable2


class Test_Term(unittest.TestCase):

    # testy zad z zaj

    # def test_stringify_teacher(self):
    #     teacherInstance = Teacher("Koko", "Roko")
    #     self.assertEqual(str(teacherInstance), "Prowadzący: Koko Roko")

    # def test_add_teacher(self):
    #     termInstance = Term(9, 30, 45, Day.FRI)
    #     termInstance.setTerm("3 II 2021 8:00 - 3 II 2021 8:30")
    #     lessonInstance = Lesson(termInstance, "koko", 2)
    #     teacherInstance = Teacher("Koko", "Roko")

    #     lessonInstance + teacherInstance

    #     self.assertEqual(lessonInstance.teacher, teacherInstance)

    # def test_remove_teacher(self):
    #     termInstance = Term(9, 30, 45, Day.FRI)
    #     termInstance.setTerm("3 II 2021 8:00 - 3 II 2021 8:30")
    #     lessonInstance = Lesson(termInstance, "koko", 2)
    #     teacherInstance = Teacher("Koko", "Roko")

    #     lessonInstance + teacherInstance

    #     self.assertEqual(lessonInstance.teacher, teacherInstance)

    #     lessonInstance - teacherInstance

    #     self.assertEqual(lessonInstance.teacher, None)

    # def test_add_teacher_too_many_hours(self):
    #     termInstance = Term(9, 30, 45, Day.FRI)
    #     termInstance.setTerm("3 II 2021 8:00 - 3 II 2021 13:30")
    #     termInstance2 = Term(9, 30, 45, Day.FRI)
    #     termInstance2.setTerm("3 II 2021 13:30 - 3 II 2021 18:00")
    #     lessonInstance = Lesson(termInstance, "koko", 2)
    #     lessonInstance2 = Lesson(termInstance, "kuku", 2)
    #     teacherInstance = Teacher("Koko", "Roko")

    #     lessonInstance + teacherInstance
    #     self.assertEqual(lessonInstance.teacher, teacherInstance)
    #     lessonInstance2 + teacherInstance
    #     self.assertEqual(lessonInstance2.teacher, None)

    # testy przygotowawcze nr.3 z poprzednich lab

    # def test_create_table(self):

    #     termInstance = Term(9, 30, 45, Day.WED)
    #     termInstance.setTerm("3 II 2021 8:00 - 3 II 2021 9:30")
    #     termInstance2 = Term(9, 30, 45, Day.THU)
    #     termInstance2.setTerm("4 II 2021 9:30 - 4 II 2021 11:00")
    #     lessonInstance = Lesson(termInstance, "koko", 2)
    #     lessonInstance2 = Lesson(termInstance2, "kuki", 2)
    #     timetableInstance = Timetable1()
    #     timetableInstance.put(lessonInstance)
    #     timetableInstance.put(lessonInstance2)
    #     timetableInstance.perform([])
    #     print(timetableInstance)

    #     self.assertEqual(len(timetableInstance.lessons), 2)
    #     self.assertEqual(timetableInstance.lessons[0].term.hour, 8)
    #     self.assertEqual(timetableInstance.lessons[0].term.minute, 0)
    #     self.assertEqual(timetableInstance.lessons[1].term.hour, 9)
    #     self.assertEqual(timetableInstance.lessons[1].term.minute, 30)

    # def test_move_ahead(self):

    #     termInstance = Term(9, 30, 45, Day.WED)
    #     termInstance.setTerm("3 II 2021 8:00 - 3 II 2021 9:30")
    #     termInstance2 = Term(9, 30, 45, Day.THU)
    #     termInstance2.setTerm("4 II 2021 9:30 - 4 II 2021 11:00")
    #     lessonInstance = Lesson(termInstance, "koko", 2)
    #     lessonInstance2 = Lesson(termInstance2, "kuki", 2)
    #     timetableInstance = Timetable1()
    #     timetableInstance.put(lessonInstance)
    #     timetableInstance.put(lessonInstance2)
    #     timetableInstance.perform(["d+", "d-", "d+", "d-"])
    #     print(timetableInstance)

    #     self.assertEqual(timetableInstance.lessons[0].term.day, Day.FRI)
    #     self.assertEqual(timetableInstance.lessons[1].term.day, Day.TUE)

    # def test_move_fail(self):

    #     termInstance = Term(9, 30, 45, Day.WED)
    #     termInstance.setTerm("3 II 2021 8:00 - 3 II 2021 9:30")
    #     termInstance2 = Term(9, 30, 45, Day.THU)
    #     termInstance2.setTerm("4 II 2021 9:30 - 4 II 2021 11:00")
    #     lessonInstance = Lesson(termInstance, "koko", 2)
    #     lessonInstance2 = Lesson(termInstance2, "kuki", 2)
    #     timetableInstance = Timetable1()
    #     timetableInstance.put(lessonInstance)
    #     timetableInstance.put(lessonInstance2)
    #     timetableInstance.perform(["d+", "d-", "d+", "d-", "d+"])
    #     print(timetableInstance)

    #     self.assertEqual(timetableInstance.lessons[0].term.day, Day.FRI)
    #     self.assertEqual(timetableInstance.lessons[1].term.day, Day.TUE)

    # testy przygotowawcze nr.1
    # def test_break_table_create(self):
    #     termInstance = Term(9, 30, 45, Day.WED)
    #     termInstance.setTerm("3 II 2021 8:00 - 3 II 2021 9:30")
    #     termInstance2 = Term(9, 30, 45, Day.FRI)
    #     termInstance2.setTerm("5 II 2021 13:00 - 5 II 2021 14:20")
    #     teacherInstance = Teacher("Koko", "Roko")
    #     lessonInstance = Lesson(termInstance, "koko", 2)
    #     lessonInstance + teacherInstance
    #     lessonInstance2 = Lesson(termInstance2, "kuki", 2, True)
    #     lessonInstance2 + teacherInstance
    #     breakInstance = Break(9, 30, 10)
    #     breakInstance2 = Break(12, 50, 10)
    #     timetableInstance = Timetable2([breakInstance, breakInstance2])
    #     timetableInstance.put(lessonInstance)
    #     timetableInstance.put(lessonInstance2)
    #     timetableInstance.perform([])
    #     print(timetableInstance)

    #     self.assertEqual(timetableInstance.breaks[0], breakInstance)
    #     self.assertEqual(timetableInstance.breaks[1], breakInstance2)
    #     self.assertEqual(timetableInstance.lessons[0].term.day, Day.WED)
    #     self.assertEqual(timetableInstance.lessons[0].term.hour, 8)
    #     self.assertEqual(timetableInstance.lessons[0].term.minute, 0)
    #     self.assertEqual(timetableInstance.lessons[0].term.duration, 90)
    #     self.assertEqual(timetableInstance.lessons[1].term.day, Day.FRI)
    #     self.assertEqual(timetableInstance.lessons[1].term.hour, 13)
    #     self.assertEqual(timetableInstance.lessons[1].term.minute, 0)
    #     self.assertEqual(timetableInstance.lessons[1].term.duration, 80)

    def test_break_fail_put(self):
        termInstance = Term(9, 30, 45, Day.WED)
        termInstance.setTerm("3 II 2021 8:00 - 3 II 2021 9:30")
        termInstance2 = Term(9, 30, 45, Day.FRI)
        termInstance2.setTerm("5 II 2021 12:55 - 5 II 2021 13:00")
        teacherInstance = Teacher("Koko", "Roko")
        lessonInstance = Lesson(termInstance, "koko", 2)
        lessonInstance + teacherInstance
        lessonInstance2 = Lesson(termInstance2, "kuki", 2)
        lessonInstance2 + teacherInstance
        breakInstance = Break(9, 30, 10)
        breakInstance2 = Break(12, 50, 10)
        timetableInstance = Timetable2([breakInstance, breakInstance2])
        timetableInstance.put(lessonInstance)
        timetableInstance.put(lessonInstance2)
        print(timetableInstance)

    def test_break_put_overdrive(self):
        termInstance = Term(9, 30, 45, Day.WED)
        termInstance.setTerm("3 II 2021 8:00 - 3 II 2021 9:30")
        termInstance2 = Term(9, 30, 45, Day.FRI)
        termInstance2.setTerm("5 II 2021 12:55 - 5 II 2021 13:00")
        teacherInstance = Teacher("Koko", "Roko")
        lessonInstance = Lesson(termInstance, "koko", 2)
        lessonInstance + teacherInstance
        lessonInstance2 = Lesson(termInstance2, "kuki", 2, True)
        lessonInstance2 + teacherInstance
        breakInstance = Break(9, 30, 10)
        breakInstance2 = Break(12, 50, 10)
        timetableInstance = Timetable2([breakInstance, breakInstance2])
        timetableInstance.put(lessonInstance)
        timetableInstance.put(lessonInstance2)
        print(timetableInstance)


if __name__ == '__main__':
    unittest.main()
