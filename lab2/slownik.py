print('Ładowanie modułu "{0}"'.format(__name__))
############################################

slownik = {}


def zapisz(string: str) -> None:
    for i in range(len(string)):
        if not string[i] in slownik:
            slownik[string[i]] = 1
            continue
        slownik[string[i]] += 1


def wypisz():
    for key, value in sorted(slownik.items()):
        print(f'{key}:{value}', end=',')


############################################
print('Załadowano moduł "{0}"'.format(__name__))
