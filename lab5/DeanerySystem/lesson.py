from day import Day
from term import Term
from teacher import Teacher


class Lesson():

    __term: Term
    __name: str
    __year: int
    __full_time: bool
    __teacher: Teacher
    __skipBreaks: bool

    def __init__(self, term: Term, name: str, year: int, skipBreaks: bool = False) -> None:

        self.term = term
        self.name = name
        self.year = year
        self.full_time = self.isFulltime()
        self.teacher = None
        self.skipBreaks = skipBreaks

    def __add__(self, teacher: Teacher) -> None:
        if self.teacher == None:
            if self.term.weekNumber not in teacher.occupation:
                teacher.occupation[self.term.weekNumber] = self.term.duration
                self.teacher = teacher
            else:
                if teacher.occupation[self.term.weekNumber] <= 6*45:
                    teacher.occupation[self.term.weekNumber] = teacher.occupation[self.term.weekNumber] + \
                        self.term.duration
                    self.teacher = teacher

    def __sub__(self, teacher: Teacher) -> None:
        if teacher == self.teacher:
            if self.term.weekNumber in teacher.occupation:
                teacher.occupation[self.term.weekNumber] = teacher.occupation[self.term.weekNumber] - \
                    self.term.duration
                self.teacher = None

    def isFulltime(self) -> bool:

        if self.term.day.value > 5:
            return False
        elif self.term.day.value < 5 or self.term.hour < 17:
            return True
        else:
            return False

    def fullTimeName(self):
        if self.full_time:
            return "stacjonarnych"
        return "niestacjonarnych"

    @property
    def term(self):
        return self.__term

    @term.setter
    def term(self, term):
        self.__term = term

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def teacherName(self):
        return self.__teacher.imie + ' ' + self.__teacher.nazwisko

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def fullTime(self) -> None:
        return self.__full_time

    @fullTime.setter
    def fullTime(self, full_time: bool) -> None:
        self.__full_time = full_time

    @property
    def teacher(self) -> None:
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher: Teacher) -> None:
        self.__teacher = teacher

    @property
    def skipBreaks(self) -> None:
        return self.__skipBreaks

    @skipBreaks.setter
    def skipBreaks(self, skipBreaks: Teacher) -> None:
        self.__skipBreaks = skipBreaks

    def earlierDay(self) -> None:
        if self.full_time and self.term.day.value > 1 and self.term.day.value < 6:
            self.term.day = Day(self.term.day.value-1)
        elif (not self.full_time) and self.term.day.value == 7:
            self.term.day = Day(self.term.day.value-1)
        elif (not self.full_time) and self.term.day.value == 6 and self.term.hour >= 17:
            self.term.day = Day(self.term.day.value-1)

    def laterDay(self) -> None:
        if self.full_time and self.term.day.value < 4:
            self.term.day = Day(self.term.day.value+1)
        elif self.full_time and self.term.day.value == 4 and self.term.hour < 17:
            self.term.day = Day(self.term.day.value+1)
        elif (not self.full_time) and self.term.day.value >= 5 and self.term.day.value < 7:
            self.term.day = Day(self.term.day.value+1)

    def earlierTime(self) -> None:

        if (not self.full_time) and self.term.day.value == 5 and (self.term.hour - self.term.duration//60) < 17:
            return

        hour = self.term.duration//60
        min = self.term.duration % 60
        poz = 0
        if self.term.minute - min < 0:
            self.term.minute = self.term.minute + 60 - min
            poz = 1
        else:
            self.term.minute = self.term.minute - min
            poz = 0

        self.term.hour = self.term.hour - poz - hour

    def laterTime(self) -> None:

        if (self.full_time) and self.term.day.value == 5 and (self.term.hour + self.term.duration//60) >= 17:
            return

        hour = self.term.duration//60
        min = self.term.duration % 60
        poz = 0

        if self.term.minute + min > 59:
            self.term.minute = self.term.minute - 60 + min
            poz = 1
        else:
            self.term.minute = self.term.minute + min
            poz = 0

        self.term.hour = self.term.hour + poz + hour

    def __str__(self) -> str:

        return (f"{self.name} ({self.term.days[self.term.day]} {self.term.startTime()}-{self.term.endTime()})\n{self.year} rok studiów {self.fullTimeName()}\nProwadzący: {self.teacherName}")
