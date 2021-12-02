import re
import sys


# usage: python3 ./zad1.py plik.c -c/--concatenate

concatenate = False
argv = sys.argv[1:]

if len(argv) > 1:
    if argv[1] == '-c' or argv[1] == '--concatenate':
        concatenate = True

try:
    file = open(argv[0], 'r')
except:
    print("Error opening file")

contents = file.read()
comments = re.findall(r"(?s)/\\*.*?\\*/", contents)
print(comments)
for comment in comments:
    if concatenate:
        result = re.sub("\n", " ", comment)
        result = re.sub("/\\*", "//", result)
        result = re.sub("\\*/", "", result)
        print(result)
    else:
        result = re.sub("\n", "\n//", comment)
        result = re.sub("/\\*", "", result)
        result = re.sub("\\*/", "", result)
        result = re.sub("", "", result)
        if result[-2] == "/":
            print(result[0:-2])
        else:
            print(result)

functions = re.findall(r"(int|float|double|void) ", contents)
print(functions)
