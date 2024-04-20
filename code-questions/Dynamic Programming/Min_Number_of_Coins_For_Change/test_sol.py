from sol import minNumberOfCoinsForChange
import unittest


class TestMinNumberOfCoinsForChange(unittest.TestCase):
    def test_coins_change(self):
        self.assertEqual(minNumberOfCoinsForChange(0, [1, 2, 5]), 0)
        self.assertEqual(minNumberOfCoinsForChange(3, [1, 2, 5]), 2)
        self.assertEqual(minNumberOfCoinsForChange(7, [1, 2, 5]), 2)
        self.assertEqual(minNumberOfCoinsForChange(11, [1, 2, 5]), 3)
        self.assertEqual(minNumberOfCoinsForChange(24, [1, 2, 5]), 6)
        self.assertEqual(minNumberOfCoinsForChange(30, [1, 2, 5]), 6)
        self.assertEqual(minNumberOfCoinsForChange(4, [2, 3, 5]), 2)
        self.assertEqual(minNumberOfCoinsForChange(7, [2, 4, 6]), -1)



if __name__ == '__main__':
    unittest.main()
