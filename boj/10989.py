# 10989번: 수 정렬하기 3
# https://www.acmicpc.net/problem/10989

# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다.
# 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
# -> 카운팅 소트!

import sys; input = sys.stdin.readline

# 입력 받으면서 쌓기
number_to_counts = [0] * 10001
n = int(input())

for _ in range(n):
    number_to_counts[int(input())] += 1

# 순서대로 출력하기
for number, count in enumerate(number_to_counts):
    for i in range(count):
        print(number)
