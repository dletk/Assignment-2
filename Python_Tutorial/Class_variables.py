class Employer:

    num_of_emps = 0
    raise_amount = 1.04 # a class variable

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
        # when access the class variable, we have to access either through the class itself
        # or through the instance of the class (aka "self")
        # if we choose "self", we will have a chance to change the value of "raise_amount" in 
        # a specific instance if we want to 

emp_1 = Employer("Mai Anh", "Nguyen", 50000) 
emp_2 = Employer("Test", "User", 60000)
print(Employer.num_of_emps) # answer is 2 


# When we try to access an attribute from an instance, it will first check 
# if the instance contains that attribute
# if it doesn't it will see if the class or any class that it inherits from
# cotains that attribute. 

emp_1.raise_amount = 1.05
print(Employer.raise_amount) # answer: 1.04
print(emp_1.raise_amount) # answer: 1.05
print(emp_2.raise_amount) # answer: 1.04







