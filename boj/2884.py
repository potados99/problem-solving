# 2884번: 알람 시계
# https://www.acmicpc.net/problem/2884

import sys; input = sys.stdin.readline


def sub_time(target: tuple, delta: tuple):
    target_h, target_m = target
    delta_h, delta_m = delta

    # 분을 빼 줍니다.
    if delta_m > target_m:
        # 만약 부족하면 1시간 빼고 60분 빌려옵니다.
        target_h -= 1
        target_m += 60

    target_m -= delta_m

    # 시를 빼 줍니다.
    if delta_h > target_h:
        # 만약 부족하면 (하루 빼고) 24시간 빌려옵니다.
        target_h += 24

    target_h -= delta_h

    return target_h, target_m


original = tuple(map(int, input().split()))

h_modified, m_modified = sub_time(original, (0, 45))

print(h_modified, m_modified)
