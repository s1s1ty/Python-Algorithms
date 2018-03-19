import unittest
from Dijkstra import Dijkstra

class DijkstraTestCase(unittest.TestCase):
    """ Test for Dijkstra.py"""
    def test(self):
        djk = Dijkstra()
        # test data 
        source = 1
        destination = 5
        djk.am[1][2] = djk.am[2][1] = 2
        djk.am[1][4] = djk.am[4][1] = 1
        djk.am[2][3] = djk.am[3][2] = 4
        djk.am[2][5] = djk.am[5][2] = 5
        djk.am[3][5] = djk.am[5][3] = 1
        djk.am[3][4] = djk.am[4][3] = 3
        
        djk.dijkstra(source)
        djk.pathPrint(destination)
        self.assertEqual(djk.sortestPath, [1,4,3,5], msg="Path Should be [1,4,3,5]")

if __name__ == '__main__':
    unittest.main()
