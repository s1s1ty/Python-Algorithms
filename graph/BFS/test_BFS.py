import unittest
from BFS import BFS

class BFSTestCase(unittest.TestCase):
    """ Test for BFS.py"""
    def test(self):
        ob = BFS()
        # test data 
        ob.am[1][2] = 1
        ob.am[1][3] = 1
        ob.am[1][5] = 1
        ob.am[3][5] = 1
        ob.am[8][4] = 1
        ob.am[2][8] = 1
        ob.am[3][4] = 1
        source = 1
        destination = 4
        ob.bfs(source)
        self.assertEqual(ob.cost_print(destination), 2, msg="Cost should be 2")

if __name__ == '__main__':
    unittest.main()

