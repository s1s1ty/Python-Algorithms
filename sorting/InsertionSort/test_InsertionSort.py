import unittest
from InsertionSort import insertionSort

class TestInsertionSort(unittest.TestCase):
    def test(self):
        case_a = ['k', 'e', 'p', 'w', 'a', 'n']
        case_b = [5,7,8,1,90,12,0]
        insertionSort(case_a)
        insertionSort(case_b)
        self.assertTrue(['a', 'e', 'k', 'n', 'p', 'w'])
        self.assertTrue([0, 1, 5, 7, 8, 12, 90])
    
if __name__ == '__main__':
    unittest.main()