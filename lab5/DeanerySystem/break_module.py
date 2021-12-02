from basicTerm import BasicTerm


class Break(BasicTerm):

    def __init__(self, hour, minute, duration):
        super().__init__(hour, minute, duration)

    def __str__(self) -> str:
        return "Przerwa"

    def __str__(self):
        if self.day == None:
            return f"{self.hour}:{self.minute} [{self.duration}]"
        return f"{str(self.day)} {self.hour}:{self.minute} [{self.duration}]"
