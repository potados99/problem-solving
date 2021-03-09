# 1931번: 회의실 배정
# https://www.acmicpc.net/problem/1931

# 알고보니 그리디였던 문제.
# 회의가 일찍 끝나는 순서대로 정렬하면 풀림.

import sys; input = sys.stdin.readline
from dataclasses import dataclass
from functools import cmp_to_key


@dataclass
class Schedule:
    begin: int
    end: int


def compare(x: Schedule, y: Schedule):
    if x.end == y.end:
        # 끝나는 시간이 같으면 일찍 시작하는 순서대로
        return x.begin - y.begin
    else:
        # 그렇지 않으면 일찍 끝나는 순서대로 정렬.
        return x.end - y.end


n = int(input())
meeting_schedules = [Schedule(*map(int, input().split())) for _ in range(n)]
meeting_schedules_sorted = sorted(meeting_schedules, key=cmp_to_key(compare))

total = 0
current_time = 0
for s in meeting_schedules_sorted:
    # 일찍 끝나는 순서대로 정렬되었기 때문에 바로 다음 스케줄이 가능하기만 하다면 최적임.
    if s.begin < current_time:
        # 이미 시작된, 소화할 수 없는 일정.
        continue

    total += 1
    current_time = s.end

print(total)
