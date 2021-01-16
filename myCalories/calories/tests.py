import unittest
from calories.services.wolfram import _get_one_attribute, get_food_data_from_wolfram


class MyTestCase(unittest.TestCase):
    def test_one_attribute(self):
        egg_1pcs_calories = _get_one_attribute('calories', 'egg', '1')
        self.assertAlmostEqual(egg_1pcs_calories, 55.0)

    def test_food_data_from_wolfram(self):
        my_food = get_food_data_from_wolfram('egg', '1')
        self.assertAlmostEqual(my_food.calories, 55.0)
        self.assertAlmostEqual(my_food.fat, 4.0)
        self.assertAlmostEqual(my_food.carbohydrates, 0.34)
        self.assertAlmostEqual(my_food.protein, 4.1)


if __name__ == '__main__':
    unittest.main()
