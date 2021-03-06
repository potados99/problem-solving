# 1152 단어의 개수
# https://www.acmicpc.net/problem/1152

# !! 문자열 시작 또는 끝에 공백이 있는 경우
# !! 단어가 0개인 경우

print(len(list(filter(lambda s: len(s) > 0, input().strip().split(' ')))))
