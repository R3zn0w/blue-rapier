from typing import Dict


class Teacher():
    __imie: str
    __nazwisko: str
    __occupation: Dict[int, int]

    @property
    def imie(self) -> str:
        return self.__imie

    @imie.setter
    def imie(self, imie: str) -> None:
        self.__imie = imie

    @property
    def nazwisko(self) -> str:
        return self.__nazwisko

    @nazwisko.setter
    def nazwisko(self, naz: str) -> None:
        self.__nazwisko = naz

    @property
    def occupation(self) -> Dict[int, int]:
        return self.__occupation

    @occupation.setter
    def occupation(self, occ: Dict[int, int]) -> None:
        self.__occupation = occ

    def __init__(self, imie: str, nazwisko: str) -> None:
        self.imie = imie
        self.nazwisko = nazwisko
        self.occupation = {}

    def __str__(self) -> str:
        return (f"Prowadzący: {self.imie} {self.nazwisko}")
