# 10951번: A+B - 4
# https://www.acmicpc.net/problem/10951

import sys; input = sys.stdin.readline

while True:
    line = input()
    if len(line) == 0:
        break

    left, right = map(int, line.split())
    print(left + right)

