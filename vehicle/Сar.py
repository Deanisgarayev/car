class Car:

    def __init__(self, model, year_manufacture, engine_capacity, price, mileage):
        self.model = model
        self.year_manufacture = year_manufacture
        self.engine_capacity = engine_capacity
        self.price = price
        self.mileage = mileage
        self.number_wheels = 4

    def description(self):
        description = (f"модель-{self.model}, год выпуска-{self.year_manufacture}, "
                       f"объем двигателя-{self.engine_capacity}, цена-{self.price},"
                       f" пробег-{self.mileage}, количество колес-{self.number_wheels}")
        return description
