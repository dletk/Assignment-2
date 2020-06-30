class Employer:

    num_of_emps = 0
    raise_amount = 1.04 

    def __init__(self, first, last, pay): 
        self.first = first 
        self.last = last
        self.email = first + "." + last + "@company.com"
        self.pay = pay

        Employer.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) 
    
    @classmethod # use classmethod decorator to create a class method
    def set_raise_amount(cls, amount): #cls is class
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay) #create new employ

    @staticmethod #use staticmethod decorator to create a static method
    def is_workday(day):
        # weekday() method in Python: Monday = 0, Sunday = 6
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employer("Mai Anh", "Nguyen", 50000)
emp_2 = Employer("User", "Test", 60000)

emp_str_1 = "John-Harrison-65000"
emp_str_2 = "Lanna-Condor-89000"
emp_str_3 = "David-Arristot-45000"

new_emp_str_1 = Employer.from_string(emp_str_1)

print(new_emp_str_1.email)

import datetime

my_date = datetime.date(2020, 6, 7)

print(Employer.is_workday(my_date))
    







