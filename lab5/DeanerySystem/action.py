from enum import Enum
from lesson import Lesson


class Action(Enum):
    TIME_EARLIER = Lesson.earlierTime
    TIME_LATER = Lesson.laterTime
    DAY_LATER = Lesson.laterDay
    DAY_EARLIER = Lesson.earlierDay
