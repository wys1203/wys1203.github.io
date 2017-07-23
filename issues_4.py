import unittest
"""
n % 3 == 0 -> 3x
n % 5 == 0 -> 5x
n % 3 == 0 and n % 5 == 0 -> 3x5x
"""


def sort():
    result = []
    n = 0
    while n <= 100:
        n += 1
        if n * 3 <= 100:
            result.append("3x")
        if n * 5 <= 100:
            result.append("5x")
        if n * 5 * 3 <= 100:
            result.append("3x5x")
    return result


class TestCaseMethods(unittest.TestCase):
    def setUp(self):
        arr = sort()
        self.my3x = arr.count("3x")
        self.my5x = arr.count("5x")
        self.my3x5x = arr.count("3x5x")

    def test_number_of_solution(self):
        nums_3x = 0
        nums_5x = 0
        nums_3x5x = 0
        for i in range(1, 101):
            if i % 3 == 0:
                nums_3x += 1
            if i % 5 == 0:
                nums_5x += 1
            if i % (3 * 5) == 0:
                nums_3x5x += 1
        self.assertEqual(nums_3x, self.my3x)
        self.assertEqual(nums_5x, self.my5x)
        self.assertEqual(nums_3x5x, self.my3x5x)


if __name__ == '__main__':
    unittest.main()
