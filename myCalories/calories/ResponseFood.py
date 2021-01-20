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
