# ----------------------------------------------------
# -- Advanced_Lessons => Unit Testing With Unittest --
# ----------------------------------------------------
# Test Runner
# - The Module that run the Unit Twsting (unittest, pytest)
# -----------------------------------------------------------
# Test Case
# - Smallest Unit of Testing
# - It Use Asserts Methods to Check for Actions and Responses
# Test Suit
# - Collection of Multiple Tests or Test Cases
# Test Report
# - A Full Report Contains The Failure or Succeed
# -----------------------------------------------------------
# unittest
# - Add Tests Into Classes as Methods
# - Use a Series of Special Assertion Methods
# https://docs.python.org/3/library/unittest.html
# -----------------------------------------------------------
import unittest

assert 3 * 8 == 24, 'Should be 24'


def test_case_one():

    assert 5 * 10 == 50, "Should be 50"


def test_case_two():
    assert 5 * 50 == 250, "Should be 50"


if __name__ == "__main__":
    test_case_one()
    test_case_two()

    print('All Tests Passed')


class MyTestCase(unittest.TestCase):
    def test_one(self):

        self.assertTrue(100 > 22, "Should be True")

    def test_two(self):
        self.assertEqual(40 + 60, 100, "Should be Equal")

    def test_three(self):
        self.assertGreter(100, 111, "Should be Greater")


if __name__ == "__main__":
    unittest.main()
