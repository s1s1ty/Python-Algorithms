import unittest
from BSTree import BSTree

class MaxHeapTestCase(unittest.TestCase):
    """ Test for Heap.py"""
    def test(self):
        tree = BSTree()
        # test data 
        # let some value for creating bs tree
        num = [11, 6, 15, 3, 8, 13, 17, 12, 14, 19, 1, 5]
        for i in num:
            tree.insert(i)

        get_inorder = tree.printInorder()
        get_preorder = tree.printPreorder()
        self.assertEqual(get_inorder, [1, 3, 5, 6, 8, 11, 12, 13, 14, 15, 17, 19], msg="Element does not matched")
        self.assertEqual(get_preorder, [11, 6, 3, 1, 5, 8, 15, 13, 12, 14, 17, 19], msg="Element does not matched")
        self.assertEqual(tree.MaxDepth(), 4, msg="Max depth of the tree does not matched")

if __name__ == '__main__':
    unittest.main()