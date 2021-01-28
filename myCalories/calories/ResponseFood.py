from calories.models import Food


class ResponseFood:
    def __init__(self, food, count):
        self.name = food.name
        self.name_pl = food.name_pl
        self.unit = food.unit
        self.calories = food.calories
        self.fat = food.fat
        self.carbohydrates = food.carbohydrates
        self.protein = food.protein
        self.count = count

    @classmethod
    def form_args(cls, calories, fats, carbohydrates, protein):
        food = Food()
        food.calories = calories
        food.fat = fats
        food.carbohydrates = carbohydrates
        food.protein = protein
        return cls(food, 0)

