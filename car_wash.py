class Car:
    def __init__(self,owner,reg,contact_num,make,model,year):
        self.owner = owner
        self.reg = reg
        self.contact_num = contact_num
        self.make = make
        self.model = model
        self.year = year
        self.is_clean = False #dirty is default status

    def __str__(self):
        return f"{self.owner}, {self.contact_num} - {self.make} {self.model} {self.year} {self.reg} Clean: {self.is_clean}"
