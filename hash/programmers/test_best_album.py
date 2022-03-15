from unittest import TestCase

from hash.programmers.best_album import solution


class Test(TestCase):
    def test_solution(self):
        result = solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500])
        self.assertTrue(result == [4, 1, 3, 0])
