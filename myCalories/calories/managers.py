from calories.models import User


def add_new_user(email, name, surname, weight, height, age):
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
    user = User.objects(email=email)
    return user
