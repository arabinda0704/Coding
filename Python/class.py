class Employee:
    def __init__(self,first,last,pay):
        self.fname=first
        self.lname=last
        self.pay=pay
        self.mail=first+"."+last+"@company.com"
emp_1=Employee("Arabinda","Das",500)
emp_2=Employee("Avik","Das",600)

# print(emp_1)
# print(emp_2)

# emp_1.first="Arabinda"
# emp_1.last="Das"
# emp_1.email="7arabinda@gmail.com"
# emp_1.pay=50000

# emp_2.first="Avik"
# emp_2.last="Das"
# emp_2.email="avik.das@gmail.com"
# emp_2.pay=600000

print(emp_1.mail)
print(emp_2.mail)

print("{} {}".format(emp_1.fname,emp_1.lname))