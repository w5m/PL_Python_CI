import unittest
import app

class MyTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(app.sum(1,1), 3)
        self.assertEqual(app.sum(1,-1), 0)
        self.assertEqual(app.sum(-1,-1), -2)
        self.assertEqual(app.sum(1.1,1), 2.1)

if __name__ == '__main__':
    unittest.main()
