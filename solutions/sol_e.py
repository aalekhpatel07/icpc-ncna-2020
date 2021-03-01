from math import sqrt
import sys


def solve(r, s):
    return round(sqrt((r * (s + 0.16))/0.067))


def main():
    for ln in sys.stdin:
        r, s = list(map(float, ln.split()))
        print(solve(r, s))


if __name__ == '__main__':
    main()
