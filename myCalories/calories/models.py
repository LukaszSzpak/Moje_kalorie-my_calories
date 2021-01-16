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
    name = StringField()
    surname = StringField()
    day_list = ListField(ReferenceField('Day'))
    height = IntField()
    age = IntField()
    weight = FloatField()


class FoodInDay(Document):
    food = ReferenceField('Food')
    how_many = FloatField()
