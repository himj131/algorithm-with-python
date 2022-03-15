from unittest import TestCase

from stack.programmers.가장큰수 import solution


class Test(TestCase):
    def test1(self):
        result = solution([6, 10, 2])
        self.assertTrue(result == '6210')

    def test2(self):
        result = solution([3, 30, 34, 5, 9])
        self.assertTrue(result == '9534330')

    def test3(self):
        result = solution([0, 0, 0])
        self.assertTrue(result == '0')

    def test4(self):
        result = solution([2])
        self.assertTrue(result == '2')

    def test5(self):
        result = solution([1000, 0, 1])
        self.assertTrue(result == '110000')
