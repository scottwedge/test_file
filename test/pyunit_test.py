import unittest
import packages

class packagesTestCase(unittest.TestCase):

    def test_small(self):
        self.assertEqual(packages.determine_cost(140,140,140,20), '5')


    def test_medium(self):
        self.assertEqual(packages.determine_cost(140,140,250,20), '7.50')

    def test_large(self):
        self.assertEqual(packages.determine_cost(140,140,350,20), '8.50')

if __name__ == '__main__':
    unittest.main()
