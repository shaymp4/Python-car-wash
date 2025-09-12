class Car:
    def __init__(self,owner,reg,contact_num,make,model,year,size):
        self.owner = owner
        self.reg = reg
        self.contact_num = contact_num
        self.make = make
        self.model = model
        self.year = year
        self.size = size
        self.is_clean = False #dirty is default status

    def __str__(self):
        return f"{self.owner}, {self.contact_num} - {self.make} {self.model} {self.year} {self.reg} Clean: {self.is_clean}"

    def make_clean(self):
        self.is_clean = True

    def make_dirty(self):
        self.is_clean = False

class CarWash:
    def __init__(self,name,small_price,large_price):
        self.name = name
        self.small_price = small_price
        self.large_price = large_price
        self.total_revenue = 0 #initialised at 0
        self.cars = [] #stores cars

    def add_car(self, car):
        self.cars.append(car)

    def dirty_cars(self):
        dirty_cars = []
        for car in self.cars:
            if not car.is_clean:
                dirty_cars.append(car)
        return dirty_cars




