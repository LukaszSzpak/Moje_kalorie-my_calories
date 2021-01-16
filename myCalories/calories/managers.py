from calories.models import User, Food, Day, FoodInDay


def add_or_change_user(email, name, surname, weight, height, age):
    user = User()
    user.email = email
    user.name = name
    user.surname = surname
    user.weight = weight
    user.height = height
    user.age = age
    user.day_list = []
    user.save()


def get_user(email):
    return User.objects(email=email)[0]


def save_user(user):
    user.save()


def add_or_change_day(date, food_list):
    day = Day()
    day.date = date
    day.food_list = food_list
    day.save()
    return day


def get_day(date):
    return Day.objects(date=date)[0]


def get_all_days():
    return Day.objects()


def save_day(day):
    day.save()


def add_or_change_food(name, name_pl, unit, calories):
    food = Food()
    food.name = name
    food.name_pl = name_pl
    food.unit = unit
    food.calories = calories
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
