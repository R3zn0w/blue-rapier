import re
import sys
from typing import Dict


def get_parts(string: str) -> Dict[str, str]:
    return {
        'words': re.findall(r'[AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻż]+', string),
        'numbers': re.findall(r'[0123456789]+', string)
    }


while 1 == 1:
    line = sys.stdin.readline()
    if line:
        result = get_parts(line)
        if result['words']:
            print("Wyraz:" + ' '.join(result['words']))
        if result['numbers']:
            print("Liczba: " + ' '.join(result['numbers']))
    else:
        break
