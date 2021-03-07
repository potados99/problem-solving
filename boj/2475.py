# 2475번: 검증수
# https://www.acmicpc.net/problem/2475

numbers = list(map(int, input().split(' ')))

sum_of_squares = sum(list(map(lambda n: n**2, numbers)))
answer = sum_of_squares % 10

print(answer)
