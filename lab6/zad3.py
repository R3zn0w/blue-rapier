import sys
from functools import reduce

print(len([x for x in filter(lambda x: int(x) % 2 == 0, reduce(
    lambda x, y: x +
    y, [open(file, 'r').read().strip().split()
        for file in sys.argv[1:]]
))]))
