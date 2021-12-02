from typing import List
from action import Action
from term import Term
from lesson import Lesson


class BasicTimetable():

    __lessons: List[Lesson]
    __trans = {'d-': Action.DAY_EARLIER, 'd+': Action.DAY_LATER,
               't-': Action.TIME_EARLIER, 't+': Action.TIME_LATER}

    def __init__(self, lessons: Lesson = []) -> None:
        self.lessons = lessons

    def parse(self, actions: List[str]) -> List[Action]:

        temp = []
        for i in range(len(actions)):
            if actions[i] in self.trans:
                temp.append(actions[i])
            else:
                raise ValueError('Translation incorrect')

        actions = []
        for i in range(len(temp)):
            actions.append(self.trans[temp[i]])
        return actions

    def perform(self, actions: List[Action]):
        index = 0
        actions_parsed = self.parse(actions)
        for i in range(len(actions_parsed)):
            index = i % len(self.lessons)
            actions_parsed[i](self.lessons[index])

    def isAhead(self, baseTerm: Term, compareTerm: Term):
        if (compareTerm.startTime(True)[0] == baseTerm.endTime(True)[0]) and (compareTerm.startTime(True)[1] >= baseTerm.endTime(True)[1]):
            return True
        elif compareTerm.startTime(True)[0] > baseTerm.endTime(True)[0]:
            return True
        return False

    def isBefore(self, baseTerm: Term, compareTerm: Term):
        if (compareTerm.endTime(True)[0] == baseTerm.startTime(True)[0]) and (compareTerm.endTime(True)[1] <= baseTerm.startTime(True)[1]):
            return True
        elif compareTerm.endTime(True)[0] < baseTerm.startTime(True)[0]:
            return True
        return False

    @ property
    def trans(self):
        return self.__trans

    @ property
    def lessons(self):
        return self.__lessons

    @ lessons.setter
    def lessons(self, lessons: List[Lesson]):
        self.__lessons = lessons
