import json
import operator
from itertools import islice

from calories.ResponseFood import ResponseFood
from calories.managers import get_all_foods_from_day_with_count, get_food

__POPULAR_COUNT = 3


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


def get_most_popular_foods_json(date_list):
    result_list = dict()
    for date in date_list:
        for food, count in get_all_foods_from_day_with_count(date):
            if food.name in result_list:
                result_list[food.name] += count
            else:
                result_list[food.name] = count

    result_list = sorted(result_list.items(), key=operator.itemgetter(1))
    result_items = list(islice(result_list, 0, __POPULAR_COUNT))

    result_foods = []
    for food, count in result_items:
        result_foods.append(json.dumps(ResponseFood(get_food(food), count).__dict__))

    return result_foods
