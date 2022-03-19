# https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3
# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.
# 제한사항
# numbers는 길이 1 이상 7 이하인 문자열입니다.
# numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
import itertools
from unittest import TestCase


def solution(str_number):
    answer = 0
    prime_numbesr = []
    numbers = [x for x in str_number]

    for i in range(1, len(numbers) + 1):
        comb = list(itertools.permutations(numbers, i))
        for nums in comb:
            if nums[0] == '0':
                continue
            number = int(''.join(nums))
            if number in prime_numbesr:
                continue
            if primenumber(number):
                prime_numbesr.append(number)
                answer = answer + 1
    return answer


def primenumber(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


class Test(TestCase):
    def test_solution1(self):
        result = solution("17")
        self.assertTrue(result == 3)

    def test_solution2(self):
        result = solution("011")
        self.assertTrue(result == 2)

    def test_util(self):
        numbers = [int(x) for x in "123"]
        print(numbers)
