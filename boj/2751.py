# 2751번: 수 정렬하기 2
# https://www.acmicpc.net/problem/2751

import sys; input = sys.stdin.readline

n = int(input())
numbers = sorted([int(input()) for _ in range(n)])

for number in numbers:
    print(number)
