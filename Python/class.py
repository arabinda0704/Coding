import datetime
class Employee:
    #Class variable
    raise_amount=1.04
    num_of_emps=0

    #class method
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount=amount
    def __init__(self,first,last,pay):
        self.fname=first
        self.lname=last
        self.pay=pay
        self.mail=first+"."+last+"@company.com"
        #class variable
        Employee.num_of_emps+=1
    def fullName(self):
        return "{} {}".format(self.fname,self.lname)
    def applyRaise():
        self.pay= int(self.pay *self.raise_amount)
    @classmethod #can be used as an alternative of constructor and it can only take class variables and can not take instance variables
    def from_string(cls,emp_str):
        first, last, pay=emp_str.split("-")
        return cls(first,last,pay)
    @staticmethod #Don't access any member of the class
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True
    
#Inheritance
class developers(Employee):
    raise_amount=1.10
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang

# print(Employee.num_of_emps)
# emp_1=Employee("Arabinda","Das",500)
# emp_2=Employee("Avik","Das",600)
# print(Employee.num_of_emps)

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

# print(emp_1.mail)
# print(emp_2.mail)

# print("{} {}".format(emp_1.fname,emp_1.lname))

# print(emp_1.fullName())
# print(emp_2.fullName())

# print(Employee.fullName(emp_1))
# print(Employee.fullName(emp_2))

# Employee.raise_amount=1.05
# emp_1.raise_amount=1.05

# Employee.set_raise_amt(1.05)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print(emp_1.__dict__)
# print(Employee.__dict__)

# emp_str_1="steve-smith-300"
# emp_str_2="Mahendra-Singh-700"

# first1, last1, pay1=emp_str_1.split("-")
# first2, last2, pay2=emp_str_2.split("-")

# new_emp_1=Employee(first1,last1,pay1)
# new_emp_2=Employee(first2,last2,pay2)

# new_emp_1=Employee.from_string(emp_str_1)
# new_emp_2=Employee.from_string(emp_str_2)

# print(new_emp_1.mail)
# print(new_emp_1.pay)

# print(new_emp_2.mail)
# print(new_emp_2.pay)

# my_date=datetime.date(2025,2,8)
# print(Employee.is_workday(my_date))

dev_1=developers("Suresh","Raina",300,"python")
dev_2=developers("Rahul","Dravid",900,"java")

# print(dev_1.mail)
# print(dev_2.pay)

print(dev_1.prog_lang)
print(dev_2.prog_lang)