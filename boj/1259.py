# 1259번: 팰린드롬수
# https://www.acmicpc.net/problem/1259

import sys; input = sys.stdin.readline

while True:
    line = input().rstrip()
    if line == '0':
        break

    if line == line[::-1]:
        print("yes")
    else:
        print("no")
