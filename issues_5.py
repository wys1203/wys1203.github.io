import unittest
"""
Try to come up as many solutions as you can
A = "hello, how are you"
B = "are"
if find then return the leading index of B else return -1
"""


def figure_out_index_of_substr(substr):
    mainstr = "hello, how are you"
    c = substr[0]
    for i, char in enumerate(mainstr):
        if char == c:
            if mainstr[i:i + len(substr)] == substr:
                return i
    return -1


class TestCaseMethods(unittest.TestCase):
    def test_case_1(self):
        r = figure_out_index_of_substr("are")
        self.assertEqual(r, 11)

    def test_case_2(self):
        r = figure_out_index_of_substr("abr")
        self.assertEqual(r, -1)


if __name__ == '__main__':
    unittest.main()
