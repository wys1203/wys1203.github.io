import unittest


def with_extra_space(arr):
    output = []
    for index in range(len(arr)):
        n = arr.pop(0)
        result = 1
        for e in arr:
            result *= e
        arr.append(n)
        output.append(result)
    return output


class TestCaseMethods(unittest.TestCase):
    def test_with_extra_space(self):
        self.assertEqual(with_extra_space([1, 2, 3, 4]), [24, 12, 8, 6])


if __name__ == '__main__':
    unittest.main()
