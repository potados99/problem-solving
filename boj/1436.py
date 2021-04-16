# 1436번: 영화감독 숌
# https://www.acmicpc.net/problem/1436

import sys; input = sys.stdin.readline


def search_until_nth(n: int):
    """
    >>> search_until_nth(2)
    1666
    """
    i = 0
    current = 665

    while i < n:
        current += 1

        if contains_666(current):
            i += 1

    return current


def contains_666(number: int):
    """
    >>> contains_666(1666)
    True
    >>> contains_666(999)
    False
    """
    return "666" in str(number)


if __name__ == "__main__":
    print(search_until_nth(int(input())))
