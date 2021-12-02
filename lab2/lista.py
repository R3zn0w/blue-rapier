print('Ładowanie modułu "{0}"'.format(__name__))
############################################

lista = []


def zapisz(string: str) -> None:
    lista.clear()
    for i in range(10):
        count = string.count(str(i))
        if count != 0:
            lista.append((i, count))


def wypisz():
    for i in range(len(lista)):
        print(str(lista[i][0])+':'+str(lista[i][1]), end=', ')


############################################
print('Załadowano moduł "{0}"'.format(__name__))
