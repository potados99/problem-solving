# 10871번: X보다 작은 수
# https://www.acmicpc.net/problem/10871

import sys; input = sys.stdin.readline

_, x = map(int, input().split())
numbers = map(int, input().split())

print(' '.join([str(n) for n in numbers if n < x]))
