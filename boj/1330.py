# 1330번: 두 수 비교하기
# https://www.acmicpc.net/problem/1330

# !! = 아니고 ==

A, B = map(int, input().split(' '))

if A < B:
    print("<")
elif A > B:
    print(">")
else:
    print("==")
