"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        pass

class Month(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
    def get_pay(self):
        return self.salary
    def __str__(self):
        return (f"{self.name} works on a monthly salary of {self.salary}. Their total pay is {get_pay(self)}.")

class Hour(Employee):
    def __init__(self, name, rate, hours):
        super().__init__(name)
        self.rate = rate
        self.hours = hours
    def get_pay(self):
        return self.rate * self.hours
    def __str__(self):
        return (f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour. Their total pay is {get_pay(self)}.")

class MonthCon(Month):
    def __init__(self, name, salary, con, com):
        super().__init__(name, salary)
        self.con = con
        self.com = com
    def get_pay(self):
        return self.salary + self.con * self.com
    def __str__(self):
        return (f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.con} contract(s) at {self.com}/contract. Their total pay is {get_pay(self)}.")

class HourCon(Hour):
    def __init__(self, name, rate, hours, con, com):
        super().__init_(name, rate, hours)
        self.con = con
        self.com = com
    def get_pay(self):
        return self.rate * self.hours + self.con * self.com
    def __str__(self):
        return (f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour and receives a commission for {self.con} contract(s) at {self.com}/contract. Their total pay is {get_pay(self)}.")

class MonthBon(Month):
    def __init__(self, name, salary, bon):
        super().__init_(name, salary)
        self.bon = bon
    def get_pay(self):
        return self.salary + self.bon
    def __str__(self):
        return (f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bon}. Their total pay is {get_pay(self)}.")

class HourBon(Hour):
    def __init__(self, name, rate, hours, bon):
        super().__init_(name, rate, hours)
        self.bon = bon
    def get_pay(self):
        return self.rate * self.hours + self.bon
    def __str__(self):
        return (f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour and receives a bonus commission of {self.bon}. Their total pay is {get_pay(self)}.")
# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
