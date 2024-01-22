
def test_passing():
    assert (1, 2, 3) == (1, 2, 3)

def test_failing():
    assert (1, 2, 3) == (3, 2, 1)

import unittest
from fibo import fibonacci

class Test(unittest.TestCase):
    def test_fibo(self):
        result = fibonacci(4)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()