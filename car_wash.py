from datetime import datetime

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
        return (f"{self.owner}, {self.contact_num} - "
                f"{self.make} {self.model} {self.year} {self.reg} Clean: {self.is_clean}")

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


    def change_small_price(self, price):
        price = input("Enter new price: ")
        self.small_price = price

    def change_large_price(self, price):
        price = input("Enter new price: ")
        self.large_price = price


    def add_car(self, car):
        self.cars.append(car)

    def dirty_cars(self):
        dirty_cars = []
        for car in self.cars:
            if not car.is_clean:
                dirty_cars.append(car)
        return dirty_cars

    def get_price(self, car):
        if car.size.lower() == "small":
            return self.small_price
        else:
            return self.large_price


    def wash(self, car):
            if car.is_clean:
                print("Car is already clean!")
            else:
                car.is_clean = True
                price = self.get_price(car)
                self.total_revenue += price
                print("Washed")


def main():
    name = input("Enter your car wash name: ")
    small_price = int(input("Enter price of a small wash: "))
    large_price = int(input("Enter price of large wash: "))
    car_wash = CarWash(name, small_price, large_price)
    menu = True

    def empty_validation(prompt):
        answer = input(prompt).strip()
        while True:
            if answer:
                return answer
            else:
                print("Can not be empty. Please try again")
                empty_validation(prompt)

    def year_validation(prompt):
        current_year = datetime.now().year
        oldest_year = 1884 #Oldest running car
        year = int(empty_validation(prompt))
        if year > current_year:
            print(f"Year must be before {current_year}. You entered {year}. ")
            year_validation(prompt)
        elif year < oldest_year:
            print(f"Year must be after {current_year}. You entered {year}. ")
            year_validation(prompt)
        elif year:
            return year
        else:
            print(f"Please enter a valid year. You entered {year}")
            year_validation(prompt)

    while(menu):
            print(f'''CAR WASH
1) Add car
2) View dirty cars
3) Wash car
4) View revenue
5) Exit''')


            user_choice = int(input("Please select an option (1/5): "))

            #ADD CAR
            if user_choice == 1:
                owner = empty_validation("Enter owners name: ")
                reg = empty_validation("Enter registration number: ")
                contact_num = empty_validation("Enter owner's contact number: ")
                make = empty_validation("Enter the make of the car: ")
                model = empty_validation("Enter the model of the car: ")
                year = year_validation("Enter the year of the car: ")
                size = empty_validation("Enter the size of the car (Small/Large): ")
                new_car = Car(owner,reg,contact_num,make,model,year,size)
                car_wash.add_car(new_car)
                print("Car added.")


            if user_choice == 2:
                dirty_cars = car_wash.dirty_cars()
                for car in dirty_cars:
                    print(car)

            if user_choice == 3:
                car_reg = input("Search registration of car to wash: ")
                for car in car_wash.cars:
                    if car_reg.lower() == car.reg.lower():
                        car_wash.wash(car)
                    else:
                        print(f"{car_reg} is not valid.")

            if user_choice == 4:
                print(car_wash.total_revenue)




if __name__ == '__main__':
    main()



