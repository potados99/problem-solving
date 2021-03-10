# 2675번: 문자열 반복
# https://www.acmicpc.net/problem/2675

import sys; input = sys.stdin.readline

n = int(input())
cases = [input().split() for _ in range(n)]

[print(''.join([c * int(case[0]) for c in case[1]])) for case in cases]
