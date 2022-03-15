# https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3
from functools import cmp_to_key


def solution(numbers):
    str_numbers = list(map(str, numbers))
    str_numbers.sort(key=cmp_to_key(compare))
    if str_numbers[0].startswith("0"):
        return "0"
    return ''.join(str_numbers)


def compare(a, b):
    if int(a + b) < int(b + a):
        return 1
    return -1
