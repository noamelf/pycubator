from interleave import interleave
import unittest


class TestGettingStartedFunctions(unittest.TestCase):
    def test_interleave(self):
        cases = [
            ([], [], []),
            ([1], [9], [1, 9]),
            ([8, 8, 3, 9], [1], [8, 1, 8, 3, 9]),
            ([2], [7, 8, 9], [2, 7, 8, 9]),
        ]

        for a, b, expected in cases:
            self.assertEqual(interleave(a, b), expected)


if __name__ == '__main__':
    unittest.main()
