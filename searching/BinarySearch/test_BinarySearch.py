import unittest
from BinarySearch import binary_search

class BinerySearchTestCase(unittest.TestCase):
    """Pre condition of Binary Search is Sorted Element of list"""
    def test(self):
        test_a = [1,3,4,6,7]
        get_result = binary_search(test_a, key=6)
        self.assertEqual(get_result[0], True, msg="Searching Fail")
        self.assertEqual(get_result[1], 3, msg="Invalid index")

        test_b = [10,20,30,40,50]
        get_result = binary_search(test_b, key=6)
        self.assertEqual(get_result[0], False, msg="Searching Fail")
        self.assertEqual(get_result[1], None, msg="Invalid index")

if __name__ == "__main__":
    unittest.main()


        
