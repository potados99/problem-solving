# 2753번: 윤년
# https://www.acmicpc.net/problem/2753

import sys; input = sys.stdin.readline


def is_multiple(number, candidate):
    """
    >>> is_multiple(2000, 100)
    True
    >>> is_multiple(14, 9)
    False
    """
    return number % candidate == 0


def is_leap_year(year: int):
    """
    윤년은,
    연도가 4의 배수이면서,
    100의 배수가 아닐 때 또는 400의 배수일 때이다.

    >>> is_leap_year(2012)
    True
    >>> is_leap_year(1900)
    False
    >>> is_leap_year(2000)
    True
    """

    if not is_multiple(year, 4):
        return False

    if not is_multiple(year, 400) and is_multiple(year, 100):
        return False

    return True


if __name__ == '__main__':
    if is_leap_year(int(input())):
        print('1')
    else:
        print('0')
