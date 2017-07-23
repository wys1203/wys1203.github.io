import unittest


def sort(n):
    arr = [1, 2, 3, 4, 5]
    i = arr.index(n)
    return arr[i::-1] + arr[i + 1:]


class TestCaseMethods(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(sort(4), [4, 3, 2, 1, 5])

    def test_case_2(self):
        self.assertEqual(sort(3), [3, 2, 1, 4, 5])


if __name__ == '__main__':
    unittest.main()
