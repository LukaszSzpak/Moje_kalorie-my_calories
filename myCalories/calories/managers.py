from calories.models import User, Food, Day, FoodInDay
from calories.sampleData.sampleUser import get_sample_user


def add_user(email, calories, fat, carbohydrates, protein, height, weight, sex, lang):
    user = User()
    user.email = email
    user.weight = weight
    user.height = height
    user.calories = calories
    user.fat = fat
    user.carbohydrates = carbohydrates
    user.protein = protein
    user.sex = sex
    user.lang = lang
    user.save()
    return user


def change_user(email, calories, fat, carbohydrates, protein, height, weight, sex, lang):
    user = get_user(email)
    user.weight = weight
    user.height = height
    user.calories = calories
    user.fat = fat
    user.carbohydrates = carbohydrates
    user.protein = protein
    user.sex = sex
    user.lang = lang
    user.save()
    return user


def get_user(email):
    users = User.objects(email=email)
    if not users:
        user = get_sample_user()
        user.save()
        return user
    return users[0]


def save_user(user):
    user.save()


def add_or_change_day(date, food_list):
    day = Day()
    day.date = date
    day.food_list = food_list
    day.save()
    return day


def get_day(date):
    days = Day.objects(date=date)
    if not days:
        return add_or_change_day(date, [])
    return days[0]


def get_all_days():
    return Day.objects()


def save_day(day):
    day.save()


def add_or_change_food(name, name_pl, unit, calories, fats, carbohydrates, proteins):
    food = Food()
    food.name = name
    food.name_pl = name_pl
    food.unit = unit
    food.calories = calories
    food.fat = fats
    food.carbohydrates = carbohydrates
    food.protein = proteins
    food.save()
    return food


def get_food(name):
    return Food.objects(name=name)[0]


def get_all_foods():
    return Food.objects()


def save_food(food):
    food.save()


def add_food_to_day(day, food, how_many):
    food_in_day = FoodInDay()
    food_in_day.food = food
    food_in_day.how_many = how_many
    food_in_day.save()

    day.food_list.append(food_in_day)
    day.save()
    return food_in_day


def get_all_foods_from_day(day_date):
    result_list = []

    day = get_day(day_date)
    food_in_day_list = day.food_list
    for food_in_day in food_in_day_list:
        result_list.append(food_in_day.food)
    return result_list


def get_all_foods_from_day_with_count(day_date):
    result_list = []

    day = get_day(day_date)
    food_in_day_list = day.food_list
    for food_in_day in food_in_day_list:
        result_list.append((food_in_day.food, food_in_day.how_many))
    return result_list
