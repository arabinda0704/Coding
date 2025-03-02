
# STRINGS

# message="Hello world"
# message=message.replace("world","Universe")
# print(message)

# greeting='Hello'
# name='Michael'

# # message='{} {}, welcome!'.format(greeting,name)
# message=f'{greeting} {name.upper()}, welcome!'

# print(message)
# print(help(str))


# NUMBERS

# num=3.449
# print(type(num))
# print(abs(num))
# print(round(num,1))
# num_1="100"
# num_2="200"
# print(int(num_1)+int(num_2))

# LISTS, TUPLES, SETS AND DICTIONARY

# courses=["Math","History"]
# courses_2=["Compsci","Geo"]
# courses.insert(1,"Arts")
# # courses.insert(0,courses_2)
# # courses.append(courses_2)

# courses.extend(courses_2)

# courses.remove("Arts")
# popped=courses.pop()
# print(popped)
# print(courses)
# courses.reverse()
# print(courses)

# courses.sort()
# print(courses)

# nums=[5,1,3,4,2,4,5,7,8,0]
# nums.sort(reverse=True)
# print(nums)
# print(8 in nums) # Returns True or False
# for index,course in enumerate(courses,start=1):# enumerate for index and value
#     print(index,course)
# course_str=" - ".join(courses)
# print(course_str)
# new_list=course_str.split(" - ")
# print(new_list)

# tuple1=("hindi","math")
# tuple2=tuple1
# print(tuple1)
# print(tuple2)
# # tuple1[0]="art"#it gives error since tuples aere immutable in nature
# # print(tuple1)

# # sets are unordered and don't contain duplicate values
# cs_courses={"hindi","Bengali","Bengali","CompSci"}#doesn't contain duplicate values it will print Bengali only once 
# print(cs_courses)#prints in unordered way
# arts_courses={"hindi","Bengali","english","Geography"}
# print(cs_courses.intersection(arts_courses))
# print(cs_courses.difference(arts_courses))
# print(cs_courses.union(arts_courses))





#FIRST CLASS FUNCTION
# def square(x):
#     return x*x
# f=square
# # print(f(5))
# def cube(x):
#     return x*x*x
# g=cube
# def my_map(fun,list):
#     result=[]
#     for i in list:
#         result.append(fun(i))
#     return result
# # squares=my_map(square,[1,2,3,4,5])
# squares=my_map(f,[1,2,3,4,5])
# cubes=my_map(g,[1,2,3,4,5])


# print(squares)
# print(cubes)

# def logger(msg):
#     def log_message():
#         print(msg)
#     return log_message
# log_hi=logger("Hi")
# log_hi()

# CLOSURE
# def outer_fun():
#     message="Hi"
#     def inner_fun():
#         print(message)
#     return inner_fun
# a=outer_fun()
# a()

#DECORATOR
# def decorator_fun(original_fun):
#     def wrapper_fun(*args,**kwargs):
#         print(f"wrapper executed this before {original_fun.__name__}")
#         return original_fun(*args,**kwargs)
#     return wrapper_fun
# @decorator_fun # no need to write ---> display=decorator_fun(display) below only display() will work in same way
# def display():
#     print("Display function ran")
# # decorator_display=decorator_fun(display)
# # decorator_display()
# display()

# @decorator_fun
# def display_info(name,age):
#     print(f"display info ran with argument {name} {age}")
# display_info("Arabinda",25)

# x=5
# print(id(x))
# y=x
# x=x+1
# print(id(x))
# z=5
# print(id(y))
# print(id(z))

student={"name":"John","age":25,"courses":['math','compsci']}
print(student["courses"])
print(student.get("Phone","Not found"))#We get none instead of keyerro if we use get method if the key doesn't exist