import getopt
import sys
import slownik
import lista

argv = sys.argv[1:]

opts, args = getopt.getopt(argv, 'm:', ['modul='])

for opt, arg in opts:
    if opt in ['-m', '--modul']:
        if arg == 'slownik':
            slownik.zapisz(args[0])
            slownik.wypisz()
        elif arg == 'lista':
            lista.zapisz(args[0])
            lista.wypisz()
