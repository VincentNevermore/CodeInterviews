
import unittest

from BST.Find_Closest_Value_In_BST.sol import BST, findClosestValueInBst


class TestClosestValueInBST(unittest.TestCase):
    def setUp(self):
        # Create a binary search tree
        self.bst = BST(10)
        self.bst.left = BST(5)
        self.bst.left.left = BST(2)
        self.bst.left.right = BST(5)
        self.bst.left.left.left = BST(1)
        self.bst.right = BST(15)
        self.bst.right.left = BST(13)
        self.bst.right.right = BST(22)
        self.bst.right.left.right = BST(14)

    def test_find_closest_value(self):
        # Test cases
        closest = findClosestValueInBst(self.bst, 12)
        self.assertEqual(closest, 13)

        closest = findClosestValueInBst(self.bst, 1)
        self.assertEqual(closest, 1)

        closest = findClosestValueInBst(self.bst, 33)
        self.assertEqual(closest, 22)

        closest = findClosestValueInBst(self.bst, 5)
        self.assertEqual(closest, 5)

        closest = findClosestValueInBst(self.bst, 14)
        self.assertEqual(closest, 14)

if __name__ == '__main__':
    unittest.main()
