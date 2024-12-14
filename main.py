from vehicle.Сar import Car
from vehicle.Truck import Truck

car = Car ("Ока", 2000, 30, 50_000, 10)
truck = Truck("Оптимус Прайм", 2001, 500, 10_000_000, 700)
print(car.description())
print(truck.description())
