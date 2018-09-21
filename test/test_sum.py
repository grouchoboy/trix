import unittest

from trix import sum


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(2, sum.sum(1, 1))
