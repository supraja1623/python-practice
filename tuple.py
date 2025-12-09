#1: Perform Basic Tuple Operations
#Create a Tuple: Create a tuple named my_tuple containing the numbers 1, 2, 3, 4, and 5.
#Access Elements: Access and print the third element of my_tuple.
#Tuple Length: Find and print the length of my_tuple.
'''my_tuple= (1, 2, 3, 4, 5)
print("tuple is:",my_tuple)
print("third element of the tuple is:",my_tuple[3])
print("length of the tuple is:",len(my_tuple))'''
#2: Tuple Repetition
'''original_tuple = ('a', 'b')
print(original_tuple*3)'''
#3: Slicing Tuples
'''numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(numbers[3:7])'''
# 4: Reverse the tuple
'''tuple1 = (10, 20, 30, 40, 50)
print(tuple1[::-1])'''
# 5: Access Nested Tuples
'''tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])'''
#6: Create a tuple with single item 50
'''tuple1=(50,)
print(tuple1)'''
#7: Unpack the tuple into 4 variables
'''tuple1 = (10, 20, 30, 40)
a,b,c,d=tuple1
print(a)
print(b)
print(c)
print(d)'''
#8: Swap two tuples in Python
'''tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1,tuple2=tuple2,tuple1
print(tuple1,tuple2)'''
#9: Copy Specific Elements From Tuple
'''tuple1 = (11, 22, 33, 44, 55, 66)
tuple2=tuple1[3:-1]
print(tuple2)'''
#10: List to Tuple
'''my_list = [10, 20, 30]
print(tuple(my_list))'''
#11: Function Returning Tuple
'''def get_min_max(numbers):
    min_value=min(numbers)
    max_value=max(numbers)
    return(max_value,min_value)
my_numbers = [10, 5, 20, 2, 15]
min_max=get_min_max(my_numbers)
print("minimum number is:",min_max)'''
#12: Comparing Tuples
'''t1 = (1, 2, 3)
t2 = (1, 2, 4)
if t1>t2:
    print(f"{t1} is greater than {t2}")
elif t1<t2:
    print(f"{t1} lessthan {t2}")
else:
    print(f"{t1} is eqaul to {t2}")'''
#13: Removing Duplicates from Tuple
'''my_tuple = (1, 2, 2, 3, 4, 4, 5)
unique=set(my_tuple)
print(tuple(unique))'''
# 14: Filter Tuples
'''students = [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('David', 95)]
print(f"Original student list: {students}")
high=[]
for i in students:
    if i[1]>=90:
        high.append(i)
print("higher achievers:",high)'''
#15: Map Tuples
'''t = (1, 2, 3, 4)
print(tuple(map(lambda x:x**2,t)))'''
#16: Modify Tuple
'''tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0]=222
print(tuple1)'''
#17: Sort a tuple of tuples by 2nd item
'''tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
list1=list(tuple1)
sorted_list= sorted(list1, key=lambda item:item[1])
print(tuple(sorted_list))'''
#18: Count Elements
'''tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))'''
#19: Check if all items in the tuple are the same
'''def check(t):
    return all(i==t[0] for i in t)
tuple1 = (45, 45, 45, 45)
print(check(tuple1))'''
