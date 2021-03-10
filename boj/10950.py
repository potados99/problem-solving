# 10950번: A+B - 3
# https://www.acmicpc.net/problem/10950

import sys; input = sys.stdin.readline

n = int(input())
cases = [tuple(map(int, input().split())) for _ in range(n)]

for case in cases:
    print(case[0] + case[1])
