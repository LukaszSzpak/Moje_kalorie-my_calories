import json

from calories.ResponseFood import ResponseFood
from calories.managers import get_all_foods_from_day_with_count


def get_weekly_nutrition_json(date_list):
    result_list = []
    for date in date_list:
        calories = 0
        fats = 0
        carbohydrates = 0
        proteins = 0

        for food, count in get_all_foods_from_day_with_count(date):
            calories += count * food.calories
            fats = count * food.fat
            carbohydrates = count * food.carbohydrates
            proteins = count * food.protein

        json_string = json.dumps(ResponseFood.form_args(calories, fats, carbohydrates, proteins).__dict__)
        result_list.append(json_string)

    return result_list
