# Unit Test example

# 1. import libraries
import unittest
from Scalculator import add, subtract, theproductofresults  # result1, result2

# 2. create test class


class MyTestClass(unittest.TestCase):
    def test_my_function(self):
        # Writing test methods
        self.assertEqual(add(2, 2), 4)
        self.assertEqual(subtract(25, 10), 15)
        self.assertIsInstance(add(2, 2), int)
        result1 = add(2, 2)
        result2 = subtract(25, 10)

        newresultproduct = theproductofresults(result1, result2)
        # When you run this test, it will check both: Whether the returned product is correctly converted to a string. Whether the type of the returned result is a string.
        self.assertIsInstance(newresultproduct, str)

        # (theproductofresults(result1, result2), str)


if __name__ == '__main__':
    unittest.main()
