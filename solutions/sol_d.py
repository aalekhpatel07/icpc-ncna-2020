import sys
from collections import Counter


def contract(word):
    if len(word) == 0:
        return ''
    i = 0
    res = [word[i]]
    curr = res[-1]
    while i < len(word):
        j = 1
        while i + j < len(word) and word[i + j] == curr:
            j += 1
        i += j
        if i == len(word):
            return ''.join(res)
        else:
            res.append(word[i])
            curr = res[-1]
    return ''.join(res)


def is_minimal(wd):
    if len(wd) == 1:
        return True
    ctr = Counter(wd)
    # print(wd, not(ctr[wd[0]] > 1 or ctr[wd[-1]] > 1))
    return not (ctr[wd[0]] > 1 or ctr[wd[-1]] > 1)


def set_equals(a, b):
    return all(x in b for x in a) and all(x in a for x in b)


def solve(word):
    _c = contract(word)
    dst = set(_c)
    if len(dst) == len(word):
        return 0
    acc = 0
    seen = set()
    for i in range(len(_c)):
        for j in range(i, len(_c)):
            if is_minimal(_c[i:j+1]):
                # print(_c[i:j+1])

                if set_equals(set(_c[i:j+1]), dst):
                    if _c[i:j+1] not in seen:
                        seen |= {_c[i:j+1]}
                        acc += 1

    return acc


def main():
    for word in sys.stdin:
        print(solve(word.strip()))
    pass


if __name__ == '__main__':
    main()
