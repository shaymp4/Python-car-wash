from datetime import datetime

class Car:
    #Basic car clss with attributes
    def __init__(self,owner,reg,contact_num,make,model,year,size,is_clean):
        self.owner = owner
        self.reg = reg
        self.contact_num = contact_num
        self.make = make
        self.model = model
        self.year = year
        self.size = size
        self.is_clean = is_clean #dirty is default status

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

    def save(self):
        with open("car_wash.txt", "w") as file:
            file.write(f"{self.name},{self.small_price},{self.large_price},{self.total_revenue}")

    @classmethod
    def load(cls):
        try:
            with open("car_wash.txt", "r") as file:
                name, small_price, large_price, revenue = file.read().split(",")
                car_wash = cls(name, float(small_price), float(large_price))
                car_wash.total_revenue = int(revenue)
                return car_wash
        except FileNotFoundError:
            print("No car wash found, please make one:")
            return create_car_wash()
        except ValueError as e:
            print(f"Error reading file. {e}")
            print("Please create a car wash...")
            return create_car_wash()

    def change_name(self, name):
        self.name = name

    def change_small_price(self, price):
        self.small_price = price

    def change_large_price(self, price):
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

    def wash(self, reg):
        for car in self.cars:
            if car.reg.lower() == reg.lower():
                if car.is_clean:
                    print(f"{reg} has already been washed.")
                else:
                    car.is_clean = True
                    price = self.get_price(car)
                    self.total_revenue += price
                    print(f"{reg} has been washed.")
                    save_car(self) #Save updated car status
                    self.save() #Save updated revenue
                return
        print(f"No car with reg: {reg} exists.")

def add_new_car(car_wash):
    #Gets user input relating to all car attributes before making a new car
    owner = empty_validation("Enter owners name: ")
    reg = empty_validation("Enter registration number: ")
    contact_num = empty_validation("Enter owner's contact number: ")
    make = empty_validation("Enter the make of the car: ")
    model = empty_validation("Enter the model of the car: ")
    year = year_validation("Enter the year of the car: ")
    size = size_validation("Enter the size of the car (Small/Large): ")
    is_clean = False #Car is dirty by default
    new_car = Car(owner, reg, contact_num, make, model, year, size, is_clean)
    car_wash.add_car(new_car)
    print(f"{owner}'s car has been added and saved.")
    save_car(car_wash)

def save_car(car_wash):
    with open("cars.txt", "w") as file:
        for car in car_wash.cars:
            file.write(f"{car.owner},{car.reg},{car.contact_num},"
                        f"{car.make},{car.model},{car.year},{car.size},{car.is_clean}\n")

def load_cars(car_wash):
    try:
        with open("cars.txt", "r") as file:
            data = file.readlines()
            for line in data:
                line = line.strip()
                if not line:
                    continue #Skip empty lines
                fields = [field.strip() for field in line.split(",")]
                if len(fields) == 8:
                    try:
                        fields[5] = int(fields[5]) #Load year in as int
                        fields[7] = fields[7].lower() == "true" #Load as bool
                        car = Car(*fields)
                        car.is_clean = fields[7]  # Sets clean status
                        car_wash.cars.append(car)
                    except ValueError as e:
                        print(f"Skipping line due to error.{line} - {e}")
                else:
                    print(f"Skipping invalid line: {line}")
    except FileNotFoundError:
        print("No file found, starting with an empty cars list.")

def view_dirty_cars(car_wash):
    dirty_cars = car_wash.dirty_cars()
    for car in dirty_cars:
        print(car)

def create_car_wash():
    #Creates an instance of a car wash.
    name = input("Enter your car wash name: ")
    small_price = float(input("Enter price of a small wash: "))
    large_price = float(input("Enter price of large wash: "))
    car_wash = CarWash(name, small_price, large_price)
    car_wash.save()
    return car_wash

def settings(car_wash):
    while True:
        try:
            print(f'''|||***SETTINGS***|||
1| Change car wash name. (Current: {car_wash.name})
2| Change small car price. (Current: {car_wash.small_price})
3| Change large price. (Current: {car_wash.large_price})
4| Go back <---''')

            user_choice = int(input("Please select an option (1/4): "))
            if user_choice == 1:
                print(f"Current name: {car_wash.name}")
                new_name = empty_validation("Please enter new car wash name: ")
                car_wash.change_name(new_name)
                car_wash.save()

            if user_choice == 2:
                while True:
                    try:
                        print(f"Current price: {car_wash.small_price}")
                        new_price = float(empty_validation("Please enter new price for small cars: "))
                        car_wash.change_small_price(new_price)
                        car_wash.save()
                        break
                    except ValueError:
                        print("Price has to be a number.")

            if user_choice == 3:
                while True:
                    try:
                        print(f"Current price: {car_wash.large_price}")
                        new_price = float(empty_validation("Please enter new price for large cars: "))
                        car_wash.change_large_price(new_price)
                        car_wash.save()
                        break
                    except ValueError:
                        print("Price has to be a number.")

            if user_choice ==4:
                return

        except ValueError:
            print("Enter a valid NUMBER (1-4)")


#***Validation Helpers****
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
            print(f"Year must be after {oldest_year_year}. You entered {year}. ")
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

def main():
    car_wash = CarWash.load()
    load_cars(car_wash)

    while True:
        try:
            print(f'''|||***{car_wash.name}***|||
1| Add car
2| View dirty cars
3| Wash car
4| View revenue
5| Settings
6| Exit''')

            user_choice = int(input("Please select an option (1/6): "))

            #ADD CAR
            if user_choice == 1:
                add_new_car(car_wash)

            if user_choice == 2:
                view_dirty_cars(car_wash)

            if user_choice == 3:
                car_reg = input("Search registration of car to wash: ")
                car_wash.wash(car_reg)

            if user_choice == 4:
                print(car_wash.total_revenue)

            if user_choice == 5:
                settings(car_wash)

            if user_choice == 6:
                print("Goodbye!")
                break
        except ValueError:
            print("Enter a NUMBER (1-5).")

if __name__ == '__main__':
    main()