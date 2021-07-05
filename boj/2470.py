# 2470번: 두 용액
# https://www.acmicpc.net/problem/2470

import sys; input = sys.stdin.readline

n = int(input())
numbers = sorted(map(lambda i: int(i), input().split()))

start = 0
end = n - 1

minimum = 2_000_000_000
minimum_two = (0, 0)

while start < end:
    sum_of_two = numbers[start] + numbers[end]

    if abs(sum_of_two) < minimum:
        # 0에 더 가까운 합이 나올 때마다 갱신
        minimum = abs(sum_of_two)
        minimum_two = (start, end)

    if sum_of_two == 0:
        # 이미 답이 나왔으면 지체하지 않고 끝내야 시간 초과를 막을 수 있음,,,
        break

    if sum_of_two > 0:
        end -= 1
    elif sum_of_two < 0:
        start += 1

print(numbers[minimum_two[0]], numbers[minimum_two[1]])
