from unittest import TestCase

import number_list
class Test(TestCase):
    def test_solution1(self):
        result = number_list.solution(["119", "97674223", "1195524421"])
        self.assertFalse(result)

    def test_solution2(self):
        result = number_list.solution(["123","456","789"])
        self.assertTrue(result)

    def test_solution3(self):
        result = number_list.solution(["12","123","1235","567","88"])
        self.assertFalse(result)



class UtilTest(TestCase):
    def test(self):
        aa = ["119", "1234", "1346", "12345"]
        aa.sort()
        print(aa)
