# 6603 로또
# https://www.acmicpc.net/problem/6603

# https://www.acmicpc.net/source/11629516 보고 감명받아 짧게 짜 보았습니다!

"""
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0
"""

from itertools import*

a = 1

while a:
    _, *a = input().split()
    [*starmap(print, combinations(a, 6))]
    print()
