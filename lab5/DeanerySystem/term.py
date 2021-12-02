from day import Day
from basicTerm import BasicTerm


class Term(BasicTerm):
    __day: Day
    weekNumber: int
    days = {
        Day.MON: "Poniedziałek",
        Day.TUE: "Wtorek",
        Day.WED: "Środa",
        Day.THU: "Czwartek",
        Day.FRI: "Piątek",
        Day.SAT: "Sobota",
        Day.SUN: "Niedziela"
    }
    romanToMonths = {
        "I": (1, 31),
        "II": (2, 28),
        "III": (3, 31),
        "IV": (4, 30),
        "V": (5, 31),
        "VI": (6, 30),
        "VII": (7, 31),
        "VIII": (8, 31),
        "IX": (9, 30),
        "X": (10, 31),
        "XI": (11, 30),
        "XII": (12, 31)
    }

    def __init__(self, hour, minute, duration=90, day=None):
        super().__init__(hour, minute, duration)
        self.day = day

    def __str__(self):
        if self.day != None:
            return f"{self.days[self.day]} {self.hour}:{self.minute} [{self.duration}]"
        return f"{self.hour}:{self.minute} [{self.duration}]"

    def earlierThan(self, termin) -> bool:
        if (self.day.difference(termin.day) > 0):
            return True
        elif (self.hour == termin.hour) and (self.hour < termin.hour):
            return True
        elif (self.minute < termin.minute):
            return True
        return False

    def laterThan(self, termin) -> bool:
        if (self.day.difference(termin.day) < 0):
            return True
        elif (self.hour > termin.hour):
            return True
        elif (self.hour == termin.hour) and (self.minute > termin.minute):
            return True
        return False

    def equals(self, termin) -> bool:
        if (self.day.difference(termin.day) == 0) and (self.hour == termin.hour) and (self.minute == termin.minute):
            return True
        return False

    def sumDays(self, day: str) -> int:
        target = self.romanToMonths[day][0]
        cnt = 1
        sum = 0
        for month in self.romanToMonths:
            if cnt == target:
                break
            sum += self.romanToMonths[month][1]
            cnt += 1

        return sum

    def minutesFromHour(self, hour: str) -> int:
        splitted = hour.split(':')
        return 60*int(splitted[0]) + int(splitted[1])

    def weekDay(self, day, month, year):
        offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        week = ['Niedziela',
                'Poniedziałek',
                'Wtorek',
                'Środa',
                'Czwartek',
                'Piątek',
                'Sobota']
        afterFeb = 1
        if month > 2:
            afterFeb = 0
        aux = year - 1700 - afterFeb
        # dayOfWeek for 1700/1/1 = 5, Friday
        dayOfWeek = 5
        # partial sum of days betweem current date and 1700/1/1
        dayOfWeek += (aux + afterFeb) * 365
        # leap year correction
        dayOfWeek += aux // 4 - aux // 100 + (aux + 100) // 400
        # sum monthly and day offsets
        dayOfWeek += offset[month - 1] + (day - 1)
        dayOfWeek %= 7
        return dayOfWeek, week[dayOfWeek]

    def numberOfWeek(self, day: int, month: int, year: int):
        offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        afterFeb = 1
        if month > 2:
            afterFeb = 0
        aux = year - 1700 - afterFeb
        # dayOfWeek for 1700/1/1 = 5, Friday
        dayOfWeek = 0
        # partial sum of days betweem current date and 1700/1/1
        dayOfWeek += (aux + afterFeb) * 365
        # leap year correction
        dayOfWeek += aux // 4 - aux // 100 + (aux + 100) // 400
        # sum monthly and day offsets
        dayOfWeek += offset[month - 1] + (day - 1)
        dayOfWeek -= (year - 1700) // 4
        weekOfYear = (dayOfWeek % 365) // 7
        return weekOfYear + 1

    def findLength(self, arr) -> int:
        yearDiff = int(arr[7])-int(arr[2])
        if yearDiff < 0:
            return -1
        if ((self.romanToMonths[arr[6]][0] - self.romanToMonths[arr[1]][0]) < 0) and yearDiff == 0:
            return -1
        elif (self.romanToMonths[arr[6]][0] - self.romanToMonths[arr[1]][0]) < 0:
            monthDiff = yearDiff * 12 - \
                (self.romanToMonths[arr[1]][0] -
                 self.romanToMonths[arr[6]][0]) % 13
        else:
            monthDiff = yearDiff * 12 + \
                self.romanToMonths[arr[6]][0] - \
                self.romanToMonths[arr[1]][0] % 13
        # validate numbers of days in month
        if (int(arr[0]) > self.romanToMonths[arr[1]][1]) or (int(arr[5]) > self.romanToMonths[arr[6]][1]):
            return -1
        if (int(arr[5]) - int(arr[0]) < 0) and monthDiff == 0:
            return -1
        else:
            day1 = self.sumDays(arr[1]) + int(arr[0])
            day2 = self.sumDays(arr[6]) + int(arr[5])
            dayDiff = yearDiff * 365 + day2 - day1
            minuteDiff = dayDiff*24*60 + \
                self.minutesFromHour(arr[8]) - self.minutesFromHour(arr[3])
            if minuteDiff < 0:
                return -1
        return minuteDiff
    # format: dzien godzina - dzien godzina

    def setTerm(self, input: str) -> bool:
        splitted = input.split()
        hourSplitted = splitted[3].split(':')
        time_len = self.findLength(splitted)
        if time_len == -1:
            print("Niepowodzenie")
            return False
        day = self.weekDay(
            int(splitted[0]), self.romanToMonths[splitted[1]][0], int(splitted[2]))
        week = self.numberOfWeek(
            int(splitted[0]), self.romanToMonths[splitted[1]][0], int(splitted[2]))
        inv_map = {v: k for k, v in self.days.items()}
        self.day = inv_map[day[1]]
        self.hour = int(hourSplitted[0])
        self.minute = int(hourSplitted[1])
        self.duration = time_len
        self.weekNumber = week
        return True

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day: Day):
        self.__day = day
