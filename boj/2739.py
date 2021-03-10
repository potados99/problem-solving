# 2739번: 구구단
# https://www.acmicpc.net/problem/2739

import sys; input = sys.stdin.readline


def print_gugu(level: int):
    left = level
    for right in range(1, 10):
        print(f"{left} * {right} = {left * right}")


n = int(input())
print_gugu(n)
