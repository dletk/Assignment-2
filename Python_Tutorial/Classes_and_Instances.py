class Employer:

    # init method/ constructor
    # when we create methods within class, they receive the instance as the first argument automatically
    # self is an instance
    def __init__(self, first, last): # first, last are other arguments
        self.first = first #it could be self.fname = fist
        self.last = last
        self.email = first + "." + last + "@company.com"

    # each method within the class automatically takes the instance (aka "self") as the first argument
    # only instance is needed as argument here
    def fullname(self):
        return "{} {}".format(self.first, self.last)


# when create Employer() downs here, the instance "self" is passed automatically 
# so we can leave off "self"
emp_1 = Employer("Mai Anh", "Nguyen") 
emp_2 = Employer("Test", "User")

# emp_1, emp_2 is passed in as self (as instance)

print(emp_1.fullname()) # since fullname() is a method, it needs ()
# don't need to pass in "self", since it is done automatically

emp_1.fullname() 
Employer.fullname(emp_1) # These two lines do the exact same things


