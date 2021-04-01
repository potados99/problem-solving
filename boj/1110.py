# 1110번: 더하기 사이클
# https://www.acmicpc.net/problem/1110

def cycle(number: int):
    number_string = str(number).rjust(2, '0')

    last_digit = number % 10
    sum_of_digits = sum([int(d) for d in number_string])
    last_digit_of_sum = sum_of_digits % 10

    return last_digit*10 + last_digit_of_sum


n = int(input())

cycled = n
count = 0
while True:
    cycled = cycle(cycled)
    count += 1

    if cycled == n:
        break

print(count)
