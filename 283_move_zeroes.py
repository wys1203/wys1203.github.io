import unittest


def move_zeros(arr):
    zeros = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            zeros += 1
        else:
            arr[i - zeros] = arr[i]
    arr[len(arr) - zeros:] = [0] * zeros
    return arr


class TestCaseMethods(unittest.TestCase):
    def test_move_zeros(self):
        self.assertEqual(move_zeros([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])


if __name__ == '__main__':
    unittest.main()
