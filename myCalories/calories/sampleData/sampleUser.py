from calories.models import User


def get_sample_user():
    user = User()
    user.email = 'default@user'
    user.weight = 60
    user.height = 160
    user.calories = 2250
    user.fat = 70
    user.carbohydrates = 300
    user.protein = 50
    user.sex = 'male'
    user.lang = 'pl'

    return user
