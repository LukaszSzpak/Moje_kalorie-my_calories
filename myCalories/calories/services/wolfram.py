import requests

from calories.models import Food
from calories.services.textCoversion import get_number_from_wolfram_response

__APP_ID = '4U9627-RPWXQY9632'


def get_food_data_from_wolfram(food_name, unit):
    food = Food()
    food.name = food_name
    food.unit = unit

    if unit == "g":
        unit = "100g"

    food.calories = _get_one_attribute('calories', food_name, unit, '')
    food.fat = _get_one_attribute('fat', food_name, unit, 'in grams')
    food.protein = _get_one_attribute('protein', food_name, unit, 'in grams')
    food.carbohydrates = _get_one_attribute('carbohydrates', food_name, unit, 'in grams')
    return food


def _get_one_attribute(attribute, food_name, unit, result_unit):
    my_param = '{0}+{1}+{2} {3}'.format(attribute, unit, food_name, result_unit)
    url = 'https://api.wolframalpha.com/v1/result?i={0}%3F&appid={1}'.format(my_param, __APP_ID)

    response = requests.get(url)
    text_response = response.text
    return get_number_from_wolfram_response(text_response)
