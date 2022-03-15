from unittest import TestCase

from stack.programmers.더맵게 import solution


class Test(TestCase):
    def test_solution(self):
        result = solution([1, 2, 3, 9, 10, 12], 7)
        self.assertTrue(result == 2)

    def test2(self):
        result = solution([1, 2], 7)
        self.assertTrue(result == -1)

    def test3(self):
        result = solution([1, 1], 3)
        self.assertTrue(result == 1)

    def test4(self):
        result = solution([1, 2, 3], 11)
        self.assertTrue(result == 2)