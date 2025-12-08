#1.Write a program to create a function that takes two arguments, name and age, and prints their values.
'''def demo(name,age):
    print(name,age)
demo("ben",20)'''
#2.Create a function with variable length of arguments
'''def func(*args):
    for arg in args:
        print(arg)
func(10,20,30,40,50)'''
#3.Write a function calculation() that accepts two variables and calculates both their addition and subtraction. The function should then return both the sum and the difference in a single return statement.
'''def calculation(a,b):
    return a+b,a-b
print(calculation(40,10))'''
#4.Write a program to create a function show_employee() with the following specifications:
'''def self_employee(name,salary=9000):
    print("name:",name,"salary:",salary )
self_employee("ben",12000)
self_employee("jessica")'''
#5: Create an inner function
#Create a program with nested functions to perform an addition calculation as follows:
'''def outer_func(a,b):
    square=a**2
    def addition(a,b):
        return a+b
    add=addition(a,b)
    return add+5
print(outer_func(5,10))'''
#6.Write a program to create a recursive function that calculates the sum of numbers from 0 to 10.

#A recursive function is a function that calls itself repeatedly.
'''def func(num):
    if num:
        return num + func(num-1)
    else:
        return 0
result=func(10)
print(result)'''
#7.Assign a different name to function and call it through the new name
'''def display_student(name,age):
    print(name,age)
student=display_student
student("sonu",20)'''
#8: Generate a Python list of all the even numbers between 4 to 30
#print(list(range(4,30,2)))
#9: Find the largest item from list
'''x = [4, 6, 8, 24, 12, 2]
print(max(x))'''
#10: Call Function using both positional and keyword arguments
'''def keyword(animal_name,pet_name):
    print(f"i have a {animal_name} named {pet_name}")
keyword("dog","lucy")
keyword(animal_name="rabbit",pet_name="jack")'''
#11: Create a function with keyword arguments
'''def print_info(**kwargs):
    if kwargs:
        print("\n--------information--------------")
        for key,value in kwargs.items():
            print(f"{key}:{value}")
    else:
        print("\n no information provided")
print_info(name="sonu",age="20",city="banglore")
print_info(job="engineer",salary=70000)'''
#13: Write a recursive function to calculate the factorial
'''def factorial(num):
    if num==0:
        return 1
    elif num<0:
        print("invalid number")
    else:
        return num*factorial(num-1)
print(factorial(6))'''
#12: Modifies global variable
'''global_variable=10
def modify():
    global global_variable
    global_variable=20
    print("inside function:",global_variable)
modify()
print("outside global variable:",global_variable)'''
#14: Create a lambda function that squares a given number
'''number=lambda x:x**2
number_1=5
square=number(number_1)
print(f"the sqaure of the number {number_1} is {square}")'''
#15: Use a lambda with the filter() function to get all even numbers from a list
'''numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x:x%2==0,numbers)))'''
#16: Use a lambda with the map() function to double each element in a list
'''numbers = [1, 2, 3, 4, 5]
print(list(map(lambda x:x*2,numbers)))'''
#17: Use a lambda with the sorted() function to sort a list of tuples based on the second element
'''data = [('apple', 5), ('banana', 2), ('cherry', 8), ('date', 1)]
print(sorted(data,key=lambda item:item[1]))'''

