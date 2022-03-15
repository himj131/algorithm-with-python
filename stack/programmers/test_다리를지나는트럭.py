from unittest import TestCase

from stack.programmers.다리를지나는트럭 import solution

class Test(TestCase):


    def test1(self):
        result = solution(2, 10, [7, 4, 5, 6])
        self.assertTrue(result == 8)

    def test2(self):
        result = solution(100, 100, [10])
        self.assertTrue(result == 101)

    def test3(self):
        result = solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
        self.assertTrue(result == 110)
