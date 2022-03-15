from unittest import TestCase

from stack.programmers.기능개발 import solution


class Test(TestCase):
    def test1(self):
        result = solution([93, 30, 55], [1, 30, 5])
        self.assertTrue(result == [2, 1])

    def test2(self):
        result = solution([95, 90, 99, 99, 80, 99],	[1, 1, 1, 1, 1, 1])
        self.assertTrue(result == [1, 3, 2])

    def test3(self):
        result = solution([1], [1])
        self.assertTrue(result == [1])

    def test4(self):
        result = solution([99], [10])
        self.assertTrue(result == [1])

    def test4(self):
        result = solution([97, 98, 95, 98, 95], [1, 1, 1, 1, 1])
        self.assertTrue(result == [2, 3])