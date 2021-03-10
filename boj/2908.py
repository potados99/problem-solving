# 2908번: 상수
# https://www.acmicpc.net/problem/2908

import sys; input = sys.stdin.readline


def reverse_digits(number: int):
    """
    >>> reverse_digits(365)
    563
    >>> reverse_digits(9999990)
    999999
    """
    acc = 0

    while number != 0:
        acc *= 10
        acc += number % 10

        number //= 10  # 정수 나눗셈

    return acc


if __name__ == '__main__':
    print(max([reverse_digits(int(n)) for n in input().split()]))
