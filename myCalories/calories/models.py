# Create your models here.


from mongoengine import *


class Food(Document):
    name = StringField(unique=True)
    name_pl = StringField()
    unit = StringField()
    calories = FloatField()
    fat = FloatField()
    carbohydrates = FloatField()
    protein = FloatField()


class Day(Document):
    date = DateField(unique=True)
    food_list = ListField(ReferenceField('FoodInDay'))


class User(Document):
    email = StringField(unique=True)
    calories = FloatField()
    fat = FloatField()
    carbohydrates = FloatField()
    protein = FloatField()
    height = FloatField()
    weight = FloatField()
    sex = StringField()
    lang = StringField()


class FoodInDay(Document):
    food = ReferenceField('Food')
    how_many = FloatField()
