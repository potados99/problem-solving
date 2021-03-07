# 1546번: 평균
# https://www.acmicpc.net/problem/1546

number_of_inputs = int(input())
scores = list(map(int, input().split(' ')))

# 점수의 최댓값이 M일 때, 각각 점수에 대해 아래 변환을 위한다:
# 점수 / M * 100
# 그리고 이들의 평균을 구한다.
# 고로 (100 * 모든 점수의 합)/(M * 점수의 갯수)를 구하면 된다.

max_scores = max(scores)
sum_scores = sum(scores)

answer = (100 * sum_scores) / (max_scores * number_of_inputs)

print(answer)
