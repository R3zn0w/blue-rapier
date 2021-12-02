class BasicTerm():
    __hour: int
    __minute: int
    __duration: int

    def __init__(self, hour: int, minute: int, duration: int):
        self.__hour = hour
        self.__minute = minute
        self.__duration = duration

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour: int):
        self.__hour = hour

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, minute: int):
        self.__minute = minute

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

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
        return BasicTerm(termin.hour, termin.minute, (self.hour - termin.hour) * 60 + self.duration + self.minute - termin.minute)

    def startTime(self, isInt: bool = False):
        if isInt:
            return (self.hour, self.minute)
        else:
            if self.minute < 10:
                return str(self.hour) + ":0" + str(self.minute)
            return str(self.hour) + ":" + str(self.minute)

    def endTime(self, isInt: bool = False):
        hour = self.duration//60
        min = self.duration % 60
        poz = 0
        if self.minute + min > 59:
            resMinute = self.minute - 60 + min
            poz = 1
        else:
            resMinute = self.minute + min
            poz = 0
        resHour = self.hour + poz + hour
        if isInt:
            return (resHour, resMinute)
        else:
            if resMinute < 10:
                return str(resHour) + ":0" + str(resMinute)
            return str(resHour) + ":" + str(resMinute)
