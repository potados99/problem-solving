# 2246번: 콘도 선정
# https://www.acmicpc.net/problem/2246

# D축으로 한번 C축으로 한번 스캔하며 반대 축으로 감소하는 점들만 추출.
# 두 번 스캔에서 모두 추출된 점들이 후보.

import sys; input = sys.stdin.readline
from dataclasses import dataclass
from functools import cmp_to_key


@dataclass(frozen=True, eq=True)
class Condo:
    distance: int
    cost: int


def compare_distance(c1: Condo, c2: Condo):
    if c1.distance == c2.distance:
        return c1.cost - c2.cost
    else:
        return c1.distance - c2.distance


def compare_cost(c1: Condo, c2: Condo):
    if c1.cost == c2.cost:
        return c1.distance - c2.distance
    else:
        return c1.cost - c2.cost


n = int(input())
condos = [Condo(*map(int, input().split())) for _ in range(n)]
condos_sorted_from_shortest = sorted(condos, key=cmp_to_key(compare_distance))
condos_sorted_from_cheapest = sorted(condos, key=cmp_to_key(compare_cost))

nominates_by_distance = set()
last_c = condos_sorted_from_shortest[0]
for c in condos_sorted_from_shortest:
    # 거리가 멀어질수록
    if c.cost <= last_c.cost:
        # 가격이 하락하는 친구들
        nominates_by_distance.add(c)
        last_c = c


nominates_by_cost = set()
last_c = condos_sorted_from_cheapest[0]
for c in condos_sorted_from_cheapest:
    # 가격이 비싸질수록
    if c.distance <= last_c.distance:
        # 거리가 가까워지는 친구들
        nominates_by_cost.add(c)
        last_c = c

nominated_both = nominates_by_distance & nominates_by_cost

print(len(nominated_both))
