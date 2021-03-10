# 10952번: A+B - 5
# https://www.acmicpc.net/problem/10952

import sys; input = sys.stdin.readline

while True:
    line = input()
    left, right = map(int, line.split())

    if left == 0 and right == 0:
        break

    print(left + right)
