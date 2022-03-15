from unittest import TestCase
import camouflage

class Test(TestCase):
    def test_solution1(self):
        result = camouflage.solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
        self.assertTrue(result == 5)

    def test_solution2(self):
        result = camouflage.solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]])
        self.assertTrue(result == 3)



class UtilTest(TestCase):
    def test1(self):
        data = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
        print(data[0])
        print(type(data[0]))
        dit = {}
        dit['dd'] ='ddd'
        print(dit)
