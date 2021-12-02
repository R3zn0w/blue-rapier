from basicTimetable import BasicTimetable
from term import Term
from lesson import Lesson
from day import Day


class Timetable1(BasicTimetable):

    def __init__(self):
        super().__init__()

    def __str__(self):
        terms = []
        display = []

        for less in self.lessons:
            terms.append(less.term)
        terms = sorted(terms, key=lambda t: t.startTime(True)[0])

        for i in range(8):
            display.append([])
            for j in range(len(terms) + 1):
                display[i].append('')

        for d in Day:
            display[d.value][0] = str(d)

        for position, term in enumerate(terms):
            display[0][position +
                       1] = f'{term.startTime()}-{term.endTime()}'

        for less in self.lessons:
            display[less.term.day.value][terms.index(
                less.term) + 1] = less.name

        separator = f'\n{"": ^12}{"":*^92}\n'
        output = ''
        for i in range(len(terms) + 1):
            for j in range(8):
                output += f'{display[j][i]: ^12}*'
            output += separator
        return output

    def can_be_transfered_to(self, term: Term, full_time: bool) -> bool:
        if not self.busy(term):
            if full_time:
                if term.day.value < 5 and term.hour >= 8 and term.hour*60+term.minute <= 60*20:
                    return True
                elif term.day.value == 5 and term.hour >= 8 and term.hour*60+term.minute <= 60*17:
                    return True
                else:
                    return False
            elif not full_time:
                if term.day.value > 5 and term.hour >= 8 and term.hour*60+term.minute <= 60*20:
                    return True
                elif term.day.value == 5 and term.hour >= 17 and term.hour*60+term.minute <= 60*20:
                    return True
                else:
                    return False
        else:
            return False

    def busy(self, term: Term) -> bool:
        for lesson in self.lessons:
            if lesson.term == term:
                return True
            if lesson.term.day == term.day:
                if (self.isAhead(lesson.term, term) == False) and (self.isBefore(lesson.term, term) == False):
                    return True
        return False

    def put(self, less: Lesson) -> bool:
        if len(self.lessons) == 0:
            self.lessons.append(less)
            return
        for i in self.lessons:
            if not self.busy(less.term):
                self.lessons.append(less)
                return
