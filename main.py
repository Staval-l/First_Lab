import argparse
from multiprocessing import Pool
import math


def square(value):
    return value ** 2


def hypotenuse(x, y):
    return math.sqrt(x + y)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="main.py")
    parser.add_argument(
        '-value_1',
        type=int,
        default=6,
        help="Это целочисленный аргумент, который подразумевает, что катет имеет значение по умолчанию")
    parser.add_argument(
        '-value_2',
        type=int,
        default=8,
        help="Это целочисленный аргумент, который подразумевает, что катет имеет значение по умолчанию")
    args = parser.parse_args()

    with Pool() as p:
        new_list = list(p.map(square, [args.value_1, args.value_2]))
    v = hypotenuse(new_list[0], new_list[1])
    print(v)
