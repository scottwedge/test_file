import unittest
import packages

class packagesTestCase(unittest.TestCase):

  def test_one(self):
    self.assertEqual(packages(140,140,140,20), '5')



if __name__ == '__main__':
    unittest.main()
