import unittest
from calories.services.wolfram import _get_one_attribute, get_food_data_from_wolfram
from calories.services.textCoversion import upper_first_letter
from calories.services.translation import translate_polish_to_english, translate_english_to_polish


class MyTestCase(unittest.TestCase):
    def test_one_attribute(self):
        egg_1pcs_calories = _get_one_attribute('calories', 'egg', '1', 'in grams')
        self.assertAlmostEqual(egg_1pcs_calories, 55.0)

    def test_food_data_from_wolfram(self):
        my_food = get_food_data_from_wolfram('egg', '1')
        self.assertAlmostEqual(my_food.calories, 55.0)
        self.assertAlmostEqual(my_food.fat, 4.0)
        self.assertAlmostEqual(my_food.carbohydrates, 0.34)
        self.assertAlmostEqual(my_food.protein, 4.1)

    def test_upper_first_letter(self):
        self.assertEqual('Jajko', upper_first_letter('jajko'))
        self.assertEqual('Drewno', upper_first_letter('drewno'))
        self.assertEqual('Imie123', upper_first_letter('imie123'))

    def test_translate_polish_to_english(self):
        self.assertEqual('egg', translate_polish_to_english('jajko'))
        self.assertEqual('wood', translate_polish_to_english('drewno'))

    def test_translate_english_to_polish(self):
        self.assertEqual('jajko', translate_english_to_polish('egg'))
        self.assertEqual('drewno', translate_english_to_polish('wood'))


if __name__ == '__main__':
    unittest.main()
