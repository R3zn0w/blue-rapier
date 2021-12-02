from day import Day


class Term():
    day: Day
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
        self.day = day
        self.hour = hour
        self.minute = minute
        self.duration = duration

    def __str__(self):
        if self.day != None:
            return f"{self.days[self.day]} {self.hour}:{self.minute} [{self.duration}]"
        return f"{self.hour}:{self.minute} [{self.duration}]"

    def __lt__(self, term):
        if self.hour < term.hour:
            return True
        elif self.minute < term.minute:
            return True
        return False

    def __le__(self, term):
        if self.hour <= term.hour:
            return True
        elif self.minute <= term.minute:
            return True
        return False

    def __sub__(self, termin):
        return Term(termin.hour, termin.minute, (self.hour - termin.hour) * 60 + self.duration + self.minute - termin.minute)

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
        inv_map = {v: k for k, v in self.days.items()}
        self.day = inv_map[day[1]]
        self.hour = hourSplitted[0]
        self.minute = hourSplitted[1]
        self.duration = time_len
        return True


term1 = Term(8, 30)
term2 = Term(9, 45, 30)
term3 = Term(9, 45, 90)
print(term1)                             # Ma się wypisać: "8:30 [90]"
print(term2)                             # Ma się wypisać: "9:45 [30]"
print(term3)                             # Ma się wypisać: "9:45 [90]"
print("term1 < term2:", term1 < term2)   # Ma się wypisać True
print("term1 <= term2:", term1 <= term2)  # Ma się wypisać True
print("term1 > term2:", term1 > term2)   # Ma się wypisać False
print("term1 >= term2:", term1 >= term2)  # Ma się wypisać False
print("term2 == term2:", term2 == term2)  # Ma się wypisać True
print("term2 == term3:", term2 == term3)  # Ma się wypisać False
term4 = term3 - term1                    # Tworzy termin, którego:
# - godzina rozpoczęcia jest taka jak 'term1',
# - czas trwania to różnica minut pomiędzy godziną zakończenia 'term3' (11:15), a godziną rozpoczęcia 'term1' (8:30)
print(term4)                             # Ma się wypisać "8:30 [165]"
