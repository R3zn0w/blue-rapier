class Klasa(object):

    tab = [1, 2, 3]

    # def __init__(self):
    #     print("Wywołano metodę '__init__()'")

    # def __init__(self, array):
    #     self.tab = array
    #     print("Wywołano metodę '__init__()'")

    def __init__(self, array, zm1, zm2):
        self.tab = array
        self._zmienna1 = zm1
        self.__zmienna2 = zm2
        print("Wywołano metodę '__init__()'")

    def __del__(self):
        print("Wywołano metodę '__del__()'")

    def __str__(self):
        return "Wywołano metodę '__str__()'"

    def __repr__(self):
        return "Wywołano metodę '__repr__()'"

    def metodaInstancyjna(self):
        print(self.tab)
        print("Wywołano metodę 'metodaInstancyjna()'")

    @classmethod
    def metodaKlasowa(cls):
        print("Wywołano metodę 'metodaKlasowa()'")

    @staticmethod
    def metodaStatyczna():
        print("Wywołano metodę 'metodaStatyczna()'")
