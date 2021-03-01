from math import log2, floor, ceil
from collections import defaultdict

PRIME = 998_244_353


def dp(n, m, t, memo):
    if m == 1:
        memo[n, m] = 1 if n <= t else 0
        return memo[n, m]
    if (n, m) in memo:
        return memo[n, m]
    acc = 0
    ub = min(t, floor(n / (2 ** (m-1))))
    skips = ceil((n - t * (2 ** m - 1))/(2 ** (m - 1)))
    lb = max(0, skips)
    if lb > ub:
        memo[n, m] = acc % PRIME
        return 0
    for p in range(lb, ub + 1):
        term = dp(n - p * (2 ** (m-1)), m-1, t, memo) % PRIME
        acc = (acc + term) % PRIME
    memo[n, m] = acc % PRIME
    # print(n, m, len(memo))
    return acc


def get_inputs():
    return list(map(int, input().split()))


def solve(n, t):
    memo = defaultdict(lambda: 0)
    d_max = 500
    dp(n, d_max, t, memo)
    ans = memo[n, d_max]
    return ans


def main():
    n, t = get_inputs()
    print(solve(n, t))
    pass


if __name__ == '__main__':
    main()
