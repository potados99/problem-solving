# 2110번: 공유기 설치
# https://www.acmicpc.net/problem/2110

import sys; input = sys.stdin.readline


def is_possible(distance: int):
    installed_routers = 0
    next_position_should_be_at_least = 0

    for position in home_positions:
        # 다음 최소 위치가 가장 끝 집보다 밖일 때
        if next_position_should_be_at_least > home_positions[-1]:
            return False

        # 아직 다음 위치에 도달하지 못 했을 때
        if position < next_position_should_be_at_least:
            continue

        next_position_should_be_at_least = position + distance
        installed_routers += 1

        # 공유기 설치가 끝났을 때
        if installed_routers >= number_of_routers:
            return True


def search(startInclusive: int, endExclusive: int):
    if startInclusive == endExclusive - 1:
        return startInclusive

    mid = (startInclusive + endExclusive) // 2

    if is_possible(mid):
        # 되면 늘리기
        return search(mid, endExclusive)
    else:
        # 안되면 줄이기
        return search(startInclusive, mid)


if __name__ == '__main__':
    n, number_of_routers = map(int, input().split())
    home_positions = sorted(int(input()) for _ in range(n))

    print(search(0, 1_000_000_000))
