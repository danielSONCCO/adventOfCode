import unittest
from fuel import getFuel, readMasses, solve

class Day1(unittest.TestCase):
    def test_getFuel(self):
        self.assertEqual(getFuel(12), 2)

    def test_readMasses(self):
        self.assertEqual(readMasses("day1/spec.txt"), [10, 20])

    def test_solve(self):
        self.assertEqual(solve("day1/spec.txt"), 5)

if __name__ == '__main__':
    unittest.main()
