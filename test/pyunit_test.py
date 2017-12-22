import unnitest
import packages

class packagesTestCase(unnitest.TestCase):

  def test_one(self):
    self.assertTrue(package(140,140,140,20), '5')



if __name__ == '__main__':
    unittest.main()
