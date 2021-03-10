# 2920번: 음계
# https://www.acmicpc.net/problem/2920

import sys; input = sys.stdin.readline

notes = map(int, input().split())

last_note = None
last_delta = None

for note in notes:
    if last_note is None:
        last_note = note
        continue

    delta = note - last_note

    if last_delta is None:
        last_note = note
        last_delta = delta
        continue

    if last_delta != delta:
        print("mixed")
        break

    last_note = note
    last_delta = delta
else:
    if last_delta > 0:
        print("ascending")
    else:
        print("descending")
