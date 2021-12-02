from day import Day
from term import Term


class Lesson():

    __term: Term
    __name: str
    __teacherName: str
    __year: int
    __full_time: bool

    def __init__(self, term: Term, name: str, teacherName: str, year: int) -> None:

        self.term = term
        self.name = name
        self.teacherName = teacherName
        self.year = year
        self.full_time = self.isFulltime()

    def isFulltime(self):

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
        return self.__teacherName

    @teacherName.setter
    def teacherName(self, name):
        self.__teacherName = name

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def fullTime(self):
        return self.__full_time

    @fullTime.setter
    def fullTime(self, full_time):
        self.__full_time = full_time

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
