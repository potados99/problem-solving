# 2562번: 최댓값
# https://www.acmicpc.net/problem/2562

import sys; input = sys.stdin.readline

numbers = [int(input()) for _ in range(9)]

max_value = max(numbers)
index_of_the_max_value = numbers.index(max(numbers))

print(max_value)
print(index_of_the_max_value + 1)
