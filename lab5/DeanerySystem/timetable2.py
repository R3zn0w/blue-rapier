from typing import List
from basicTimetable import BasicTimetable
from term import Term
from lesson import Lesson
from action import Action
from day import Day
from teacher import Teacher
from break_module import Break


class Timetable2(BasicTimetable):

    __breaks: List[Break]

    @property
    def breaks(self):
        return self.__breaks

    @breaks.setter
    def breaks(self, break_item: Break):
        self.__breaks.append(break_item)

    def __init__(self, breaks: List[Break]):
        super().__init__()
        self.__breaks = breaks

    def __str__(self):
        terms = []
        display = []
        starthours = []

        for less in self.lessons:
            terms.append(less.term)
            starthours.append(less.term.startTime(True))

        for bre in self.breaks:
            terms.append(bre)
            starthours.append(bre.startTime(True))
        starthours.sort()
        terms = sorted(terms, key=lambda t: t.startTime(True))
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

        for bre in self.breaks:
            for day in range(1, 8):
                display[day][starthours.index(
                    bre.startTime(True)) + 1] = '-----'

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

    def busy(self, term: Term, skipBreaks: bool) -> bool:
        for lesson in self.lessons:
            if lesson.term == term:
                return True
            if lesson.term.day == term.day:
                if (self.isAhead(lesson.term, term) == False) and (self.isBefore(lesson.term, term) == False):
                    return True
        if not skipBreaks:
            for bre in self.breaks:
                if bre == term:
                    return True
                if (self.isAhead(bre, term) == False) and (self.isBefore(bre, term) == False):
                    return True
        return False

    def put(self, less: Lesson) -> bool:
        if len(self.lessons) == 0:
            self.lessons.append(less)
            return
        for i in self.lessons:
            if not self.busy(less.term, less.skipBreaks):
                self.lessons.append(less)
                return
