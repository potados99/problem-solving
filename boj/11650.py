# 11650번: 좌표 정렬하기
# https://www.acmicpc.net/problem/11650

import sys; input = sys.stdin.readline
from dataclasses import dataclass
from functools import cmp_to_key


@dataclass
class Coordinate:
    x: int
    y: int


def compare(c1: Coordinate, c2: Coordinate):
    if c1.x == c2.x:
        return c1.y - c2.y
    else:
        return c1.x - c2.x


n = int(input())
coordinates = sorted([Coordinate(*map(int, input().split())) for _ in range(n)], key=cmp_to_key(compare))

for c in coordinates:
    print(c.x, c.y)
