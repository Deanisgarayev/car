from vehicle.Сar import Car

class Truck(Car):
    def __init__(self, model, year_manufacture, engine_capacity, price, mileage):
        super().__init__(model, year_manufacture, engine_capacity, price, mileage)
        self.number_wheels = 8

    def description(self):
        description = (f"модель-{self.model}, год выпуска-{self.year_manufacture}, "
                       f"объем двигателя-{self.engine_capacity}, цена-{self.price},"
                       f" пробег-{self.mileage}, количество колес-{self.number_wheels}")
        return description
