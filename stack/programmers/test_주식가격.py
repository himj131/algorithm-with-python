from unittest import TestCase

from stack.programmers.주식가격 import solution


class Test(TestCase):
    def test1(self):
        result = solution([1, 2, 3, 2, 3])
        self.assertTrue(result == [4, 3, 1, 1, 0])

    def test2(self):
        result = solution([1, 1])
        self.assertTrue(result == [1, 0])

    def test3(self):
        result = solution([5, 3, 6, 7])
        self.assertTrue(result == [1, 2, 1, 0])
