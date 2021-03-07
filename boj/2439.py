# 2439번: 별 찍기 - 2
# https://www.acmicpc.net/problem/2439

number_of_lines = int(input())

for i in range(number_of_lines):
    print(" "*(number_of_lines-(i+1)) + "*"*(i+1))
