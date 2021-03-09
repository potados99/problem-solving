# 9498번: 시험 성적
# https://www.acmicpc.net/problem/9498

# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D,
# 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

import sys; input = sys.stdin.readline

grades_to_score_ranges = {
    'A': (90, 100),
    'B': (80, 89),
    'C': (70, 79),
    'D': (60, 69),
    'F': (0, 59)
}

score = int(input())

for grade, score_range in grades_to_score_ranges.items():
    print(grade) if score_range[0] <= score <= score_range[1] else None
