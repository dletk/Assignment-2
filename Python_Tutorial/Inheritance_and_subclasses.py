class Employer:

    raise_amount = 1.04 

    def __init__(self, first, last, pay): 
        self.first = first 
        self.last = last
        self.email = first + "." + last + "@company.com"
        self.pay = pay

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) 

class Developer(Employer): # subclass Developer inherited from Employer class
    raise_amount = 1.10 # change raise amount in Developer subclass. 
    # It doesn't change raise amount in Employer class

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # pass first, last, pay from Employer class to subclass
        # can also do: Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employer):
    def __init__(self, first, last, pay, employees = None): #list of employees, set default to None
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = [] # empty list
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("-->", emp.fullname())


dev_1 = Developer("Mai Anh", "Nguyen", 50000, "Python")
dev_2 = Developer("User", "Test", 60000, "Java")

mng_1 = Manager("Sue", "Smith", 90000, [dev_1])

# isinstance() tell us if an object is an instance of a class
print(isinstance(mng_1, Employer)) # answer: True
print(isinstance(mng_1, Manager)) # answer: True
print(isinstance(mng_1, Developer)) # answer: False

# issubclass() tell us if a class is a subclass of the other
print(issubclass(Manager, Employer)) #answer: True
print(issubclass(Manager, Developer)) #answer: False






    







