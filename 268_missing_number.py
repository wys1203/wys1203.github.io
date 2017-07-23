import unittest


def my_solution(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    for i, n in enumerate(nums):
        if i != n:
            return i
    return i + 1


def func2(nums):
    return set(list(range(len(nums) + 1))).difference(set(nums)).pop()


def func3(nums):
    s = int((len(nums) + 1) * len(nums) / 2)
    return s - sum(nums)


class TestCaseMethods(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(my_solution([0]), 1)
        self.assertEqual(func2([0]), 1)
        self.assertEqual(func3([0]), 1)

    def test_case_2(self):
        self.assertEqual(my_solution([0, 1]), 2)
        self.assertEqual(func3([0, 1]), 2)
        self.assertEqual(func3([0, 1]), 2)

    def test_case_3(self):
        self.assertEqual(my_solution([1, 0]), 2)
        self.assertEqual(func3([1, 0]), 2)
        self.assertEqual(func3([1, 0]), 2)

    def test_case_4(self):
        self.assertEqual(my_solution([0, 1, 2, 4]), 3)
        self.assertEqual(func3([0, 1, 2, 4]), 3)
        self.assertEqual(func3([0, 1, 2, 4]), 3)


if __name__ == '__main__':
    unittest.main()
