from unittest import TestCase

from stack.programmers.프린터 import solution


class Test(TestCase):
    def test1(self):
        result =solution([2, 1, 3, 2],2)
        self.assertTrue(result == 1)

    def test2(self):
        result = solution([1, 1, 9, 1, 1, 1], 0)
        self.assertTrue(result == 5)
