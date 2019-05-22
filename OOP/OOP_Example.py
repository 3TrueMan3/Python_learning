class Car:
    name = "c200"
    make = "mercedes"
    model = 2008

    def start(self):
        print("Заводим двигатель")

    def stop(self):
        print("Глушим двигатель")

car_a = Car()
car_b = Car()

car_a.start()
print(car_a.model,  car_a.make, car_a.name)
car_a.stop()