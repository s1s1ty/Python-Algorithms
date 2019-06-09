import unittest

from MergeSort import merge_sort


class TestMergeSort(unittest.TestCase):
    def test(self):
        case_1 = [6, 5, 4, 3, 2, 1]
        case_2 = [2, 3, 1, 5, 6, 4]
        merge_sort(case_1)
        merge_sort(case_2)

        self.assertEqual([1, 2, 3, 4, 5, 6], case_1)
        self.assertEqual([1, 2, 3, 4, 5], case_2)


if __name__ == "__main__":
    unittest.main()
