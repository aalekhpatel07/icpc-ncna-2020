import sys


def get_inputs():
    tf = float(input())
    tr = float(input())
    res = []
    for num in sys.stdin:
        num = float(num.strip())
        res.append(num)
    return tf, tr, res


def solve():
    tf, tr, inputs = get_inputs()
    res = []
    for idx, _v in enumerate(inputs):
        if 0 < _v < 1:
            res.append(1)
            continue
        _fl = int(_v)
        if _v <= _fl + tf:
            res.append(_fl)
        elif _v >= _fl + tr:
            res.append(_fl + 1)
        else:
            for _i in range(idx, -1, -1):
                if _fl + tf <= inputs[_i] <= _fl + tr:
                    continue
                else:
                    if inputs[_i] > _fl + tr:
                        res.append(_fl + 1)
                    else:
                        res.append(_fl)
                    break
    return res


def main():
    ans = solve()
    for x in ans:
        print(x)
    return


if __name__ == '__main__':
    main()
