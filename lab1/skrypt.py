import sys


def is_prime(num: int) -> bool:
    try:
        num = int(num)
    except:
        return False
    for i in range(2, (num//2)+1):
        if num % i == 0:
            return False
    else:
        return True


for i in range(1, len(sys.argv)):
    if is_prime(sys.argv[i]):
        print(sys.argv[i])
