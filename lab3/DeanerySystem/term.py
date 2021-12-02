from day import Day


class Term():
    day: Day
    days = {
        Day.MON: "Poniedzialek",
        Day.TUE: "Wtorek",
        Day.WED: "Środa",
        Day.THU: "Czwartek",
        Day.FRI: "Piątek",
        Day.SAT: "Sobota",
        Day.SUN: "Niedziela"
    }

    def __init__(self, day, hour, minute):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.duration = 90

    def __str__(self):
        return f"{self.days[self.day]} {self.hour}:{self.minute} [{self.duration}]"

    def earlierThan(self, termin):
        if (self.day.difference(termin.day) > 0):
            return True
        elif (self.hour == termin.hour) and (self.hour < termin.hour):
            return True
        elif (self.minute < termin.minute):
            return True
        return False

    def laterThan(self, termin):
        if (self.day.difference(termin.day) < 0):
            return True
        elif (self.hour > termin.hour):
            return True
        elif (self.hour == termin.hour) and (self.minute > termin.minute):
            return True
        return False

    def equals(self, termin):
        if (self.day.difference(termin.day) == 0) and (self.hour == termin.hour) and (self.minute == termin.minute):
            return True
        return False
