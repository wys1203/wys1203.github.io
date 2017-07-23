import unittest


def pick(s):
    n = []
    for c in set(s):
        if s.count(c) == 1:
            n.append(s.index(c))
    if len(n) > 0:
        return min(n)
    else:
        return -1


class TestCaseMethods(unittest.TestCase):
    def test_pick_case_1(self):
        self.assertEqual(pick("leetcode"), 0)

    def test_pick_case_2(self):
        self.assertEqual(pick("loveleetcode"), 2)

    def test_pick_case_3(self):
        self.assertEqual(pick(""), -1)

    def test_pick_case_4(self):
        self.assertEqual(pick("z"), 0)

    def test_pick_case_5(self):
        self.assertEqual(pick("cc"), -1)

    def test_pick_case_6(self):
        self.assertEqual(pick("aaddadaaaa"), -1)


if __name__ == '__main__':
    unittest.main()
