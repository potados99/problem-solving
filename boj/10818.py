# 10818번: 최소, 최대
# https://www.acmicpc.net/problem/10818

import sys; input = sys.stdin.readline

input()
numbers = list(map(int, input().split()))

print(min(numbers), max(numbers))
