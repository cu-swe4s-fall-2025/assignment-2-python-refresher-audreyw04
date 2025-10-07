import unittest
import my_utils
import random
import os


class TestMyUtils(unittest.TestCase):

    def test_calculate_mean_random(self):
        data = [random.randint(-100, 100) for _ in range(20)]
        result = my_utils.calculate_mean(data)
        self.assertIsInstance(result, float)

    def test_calculate_median_random(self):
        data = [random.randint(-100, 100) for _ in range(21)]
        result = my_utils.calculate_median(data)
        self.assertIsInstance(result, float)

    def test_calculate_sd_random(self):
        data = [random.randint(-100, 100) for _ in range(15)]
        mean = my_utils.calculate_mean(data)
        result = my_utils.calculate_sd(data, mean)
        self.assertIsInstance(result, float)

    def test_calculate_mean(self):
        self.assertEqual(my_utils.calculate_mean([1, 2, 3]), 2.0)
        self.assertEqual(my_utils.calculate_mean([]), 0.0)

        # Negative: single value
        self.assertEqual(my_utils.calculate_mean([5]), 5.0)

    def test_calculate_median(self):
        self.assertEqual(my_utils.calculate_median([1, 2, 3]), 2.0)
        self.assertEqual(my_utils.calculate_median([1, 2, 3, 4]), 2.5)
        self.assertEqual(my_utils.calculate_median([]), 0.0)

        # Negative: single value
        self.assertEqual(my_utils.calculate_median([7]), 7.0)

    def test_calculate_sd(self):
        data = [1, 2, 3]
        mean = my_utils.calculate_mean(data)
        self.assertAlmostEqual(my_utils.calculate_sd(data, mean),
                               0.816496580927726)
        self.assertEqual(my_utils.calculate_sd([], 0), 0.0)

        # Negative: single value (should be 0.0)
        self.assertEqual(my_utils.calculate_sd([5], 5.0), 0.0)
