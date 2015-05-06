import unittest
import bubble

class TesteBubble(unittest.TestCase):
    
    def test_bubble(self):
        list = [1,30,2,5,3]
        bubble.bubbleSort(list)
        self.assertEquals(list, [1,2,3,5,30])


if __name__ == '__main__':
    unittest.main()