from datetime import datetime

class Car:
    #Basic car clss with attributes
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
        return (f"""**{self.reg.upper()}**
Owner: {self.owner}
Contact Number: {self.contact_num}
Make: {self.make}
Model: {self.model} 
Manufacture Year:{self.year} 
Clean: {self.is_clean}""")

    def make_clean(self):
        self.is_clean = True

    def make_dirty(self):
        self.is_clean = False

class CarWash:
    #Basic car wash class with attributes and business methods
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
        #Groups together all dirty cars
        dirty_cars = []
        for car in self.cars:
            if not car.is_clean:
                dirty_cars.append(car)
        return dirty_cars

    def get_price(self, car):
        if car.size.lower() == "small":
            return self.small_price
        elif car.size.lower() == "large":
            return self.large_price
        else:
            print("No price available.")

    def wash(self, car):
        #Checks if a car is dirty before washing.
            if car.is_clean:
                print("Car is already clean!")
            else:
                car.is_clean = True
                price = self.get_price(car)
                self.total_revenue += price
                print("Washed")


def main():

    def save_car(car):
        with open("cars.txt", "a") as file:
            file.write(f"{car.owner},{car.reg},{car.contact_num},"
                        f"{car.make},{car.model},{car.year},{car.size} \n")
            print("car has been saved to cars.txt")

    def load_cars():
        with open("cars.txt", "r") as file:
            data = file.readlines()
            for line in data:
                if line:
                    fields = [field.strip() for field in line.split(",")]
                    if len(fields) == 7:
                        fields[5] = int(fields[5]) #Load year in as int
                        car = Car(*fields)
                        car_wash.cars.append(car)
                    else:
                        print(f"Skipping line: {line}")

    def create_car_wash():
        #Creates an instance of a car wash.
        name = input("Enter your car wash name: ")
        small_price = int(input("Enter price of a small wash: "))
        large_price = int(input("Enter price of large wash: "))
        return CarWash(name, small_price, large_price)

    def empty_validation(prompt):
        #Ensures user input is not left empty, will loop until field is not empty
        while True:
            answer = input(prompt).strip()
            if answer:
                return answer
            else:
                print("Can not be empty. Please try again")

    def year_validation(prompt):
        #Checks a year making sure it cant be before 1884 or after current year
        while True:
            current_year = datetime.now().year
            oldest_year = 1884 #Oldest running car
            year = int(empty_validation(prompt)) #Ensures year is not empty
            if year > current_year:
                print(f"Year must be before {current_year}. You entered {year}. ")
            elif year < oldest_year:
                print(f"Year must be after {current_year}. You entered {year}. ")
            elif year:
                return year
            else:
                print(f"Please enter a valid year. You entered {year}")

    def size_validation(prompt):
        #Ensures a user only enters valid sizes
        while True:
            size = empty_validation(prompt).lower()
            if size in ["small", "large"]:
                return size
            else:
                print("Size must be 'small' or 'large'")
                print(f"You entered {size}")

    def add_new_car():
        #Gets user input relating to all car attributes before making a new car
        owner = empty_validation("Enter owners name: ")
        reg = empty_validation("Enter registration number: ")
        contact_num = empty_validation("Enter owner's contact number: ")
        make = empty_validation("Enter the make of the car: ")
        model = empty_validation("Enter the model of the car: ")
        year = year_validation("Enter the year of the car: ")
        size = size_validation("Enter the size of the car (Small/Large): ")
        new_car = Car(owner, reg, contact_num, make, model, year, size)
        car_wash.add_car(new_car)
        print("Car added.")
        save_car(new_car)

    def view_dirty_cars():
        dirty_cars = car_wash.dirty_cars()
        for car in dirty_cars:
            print(car)

    car_wash = create_car_wash()
    load_cars()

    while True:
            print(f'''CAR WASH
1) Add car
2) View dirty cars
3) Wash car
4) View revenue
5) Exit''')


            user_choice = int(input("Please select an option (1/5): "))

            #ADD CAR
            if user_choice == 1:
                add_new_car()


            if user_choice == 2:
                view_dirty_cars()

            if user_choice == 3:
                car_reg = input("Search registration of car to wash: ")
                found = False
                for car in car_wash.cars:
                    if car_reg.lower() == car.reg.lower():
                        car_wash.wash(car)
                        found = True
                        break
                if not found:
                    print(f"{car_reg} is not valid.")


            if user_choice == 4:
                print(car_wash.total_revenue)




if __name__ == '__main__':
    main()



