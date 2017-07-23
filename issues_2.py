import unittest


def sort(n):
    arr = [1, 2, 3, 4, 5]
    n = arr.pop(arr.index(n))
    return [n] + arr


class TestCaseMethods(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(sort(3), [3, 1, 2, 4, 5])

    def test_case_2(self):
        self.assertEqual(sort(4), [4, 1, 2, 3, 5])


if __name__ == '__main__':
    unittest.main()
