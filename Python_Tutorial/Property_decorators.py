class Employer:

    def __init__(self, first, last): 
        self.first = first 
        self.last = last
    
    @property # add decorator property
    def email(self):
        return "{}.{}.@company.com".format(self.first, self.last)
    
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    @fullname.deleter # create a setter
    def fullname(self):
        print("Delete Name")
        self.first = None
        self.last = None


emp_1 = Employer("Mai Anh", "Nguyen")
    
del emp_1.fullname

print(emp_1.first) # asnwer: None