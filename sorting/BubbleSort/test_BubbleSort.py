import unittest
from BubbleSort import bubbleSort

class TestBubbleSort(unittest.TestCase):
    def test(self):
        case_a = ['k', 'e', 'p', 'w', 'a', 'n']
        case_b = [5,7,8,1,90,12,0]
        bubbleSort(case_a)
        bubbleSort(case_b)
        self.assertTrue(['a', 'e', 'k', 'n', 'p', 'w'])
        self.assertTrue([0, 1, 5, 7, 8, 12, 90])

if __name__ == "__main__":
    unittest.main()
