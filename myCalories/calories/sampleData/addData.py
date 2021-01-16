from calories.managers import *
import datetime


def add_sample_data():
    Day.drop_collection()
    Food.drop_collection()
    FoodInDay.drop_collection()

    day = Day()
    food = Food()

    food.name = 'Egg'
    food.name_pl = 'Jajko'
    food.calories = 200
    food.unit = 'pcs'
    food.fat = 5.5
    food.protein = 3.5
    food.carbohydrates = 2.7
    food.save()

    day.date = datetime.date.today()
    day.save()

    add_food_to_day(day, food, 5)
