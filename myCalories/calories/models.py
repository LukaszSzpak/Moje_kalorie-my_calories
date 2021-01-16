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

    def __str__(self):
        return '{0}, {1}'.format(self.name, self.unit)


class Day(Document):
    date = DateField(unique=True)
    food_list = ListField(ReferenceField('Food'))

    def __str__(self):
        return '{0}, food count:{1}'.format(self.date, len(self.food_list))


class User(Document):
    email = StringField(unique=True)
    name = StringField()
    surname = StringField()
    day_list = ListField(ReferenceField('Day'))
    height = IntField()
    age = IntField()
    weight = FloatField()

    def __str__(self):
        return '{0}, {1}, days count:{2}'.format(self.name, self.surname, len(self.day_list))
