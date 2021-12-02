def toFloat(arg: str) -> float:
    try:
        return float(arg)
    except ValueError:
        raise Exception("String is not convertible to number")


def sum(arg1: str, arg2: str) -> float:
    if isinstance(arg1, str):
        arg1 = toFloat(arg1)
    if isinstance(arg2, str):
        arg2 = toFloat(arg2)
    try:
        return arg1 + arg2
    except TypeError:
        raise Exception("Invalid type")


if __name__ == '__main__':
    print(f'suma = {sum(1.7, 6)}')
