import unittest

from QuickSort import quick_sort


class TestQuickSort(unittest.TestCase):
    def test(self):
        case_1 = [4, 3, 5, 2, 8, 0]
        quick_sort(case_1)
        self.assertEqual([0, 2, 3, 4, 5, 8], case_1)


if __name__ == "__main__":
    unittest.main()
