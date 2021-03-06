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
    
    def __repr__(self):
        return  "Employer('{}', '{}', '{}')".format(self.first, self.last, self.pay)
    
    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employer("Mai Anh", "Nguyen", 50000)
emp_2 = Employer("User", "Test", 60000)

print(len(emp_1))  # answer: 14







