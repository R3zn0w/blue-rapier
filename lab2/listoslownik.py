import lista
import slownik
import sys

if len(sys.argv) < 3:
    print("Invalid number of parameters")
    sys.exit()

if sys.argv[1] == "--lista":
    lista.zapisz(sys.argv[2])
    lista.wypisz()

if sys.argv[1] == "--slownik":
    slownik.zapisz(sys.argv[2])
    slownik.wypisz()
