import unittest
from alarm_1202 import readSequence, runProgram, decodeAnswer

class Day2(unittest.TestCase):
    def test_readSequence(self):
        self.assertEqual(readSequence("day2/spec.txt"), [1, 2, 3])

    def test_runProgram(self):
        sequence = [1, 0, 0, 0, 99]
        runProgram(sequence)
        self.assertEqual(
            sequence,
            [2, 0, 0, 0, 99]
        )
        sequence = [1,1,1,4,99,5,6,0,99]
        runProgram(sequence)
        self.assertEqual(sequence, [30,1,1,4,2,5,6,0,99])

    def test_decodeAnswer(self):
        self.assertEqual(decodeAnswer(4945026), 1202)

if __name__ == '__main__':
    unittest.main()
