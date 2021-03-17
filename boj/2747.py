# 2747번: 피보나치 수
# https://www.acmicpc.net/problem/2747

import sys; input = sys.stdin.readline


cache = {}


def fibonacci(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    if n in cache:
        return cache[n]

    result = fibonacci(n - 1) + fibonacci(n - 2)
    cache[n] = result

    return result


print(fibonacci(int(input())))
