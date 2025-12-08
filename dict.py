#1: Perform basic dictionary operations
#Perform following operations on given dictionary
#Add New Key-Value Pair: Add a new key-value pair, 'profession': 'Doctor', to the dictionary and print the updated dictionary.
#Modify Value: Change the value of the age key to 40 in the dictionary and print the updated dictionary.
#Access Key: Print the value associated with the city key.
'''my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
my_dict['profession']="doctor"
print("updated dictionary:",my_dict)
my_dict['age']=40
print("updated dictionary:",my_dict)'''
#2: Perform dictionary operations
#Remove Key-Value Pair : Remove the profession key-value pair from the dictionary.
#Get Items (Key-Value Pairs): Print all key-value pairs (items) in the dictionary.
#Check if Key Exists in the dictionary
'''my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
del my_dict['profession']
print(my_dict)
print(my_dict.items())
key='profession'
if key in my_dict:
    print("key is present")
else:
    print("key is not present")'''
#3: Dictionary from Lists
'''keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
print(dict(zip(keys,values)))'''
#4: Clear Dictionary
'''my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
my_dict.clear()
print(my_dict)'''
#5: Merge two Python dictionaries into one
'''dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3={**dict1,**dict2}
print(dict3)'''
#7: Access Nested Dictionary
'''data = {'person': {'name': 'Alice', 'age': 30}}
alices_age=data['person']['age']
print(alices_age)'''
#8: Print the value of key ‘history’ from nested dict
'''sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
history_class=sampleDict['class']['student']['marks']['history']
print(history_class)'''
#9: Modify Nested Dictionary
'''nested_student_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
nested_student_dict['class']['student']['name']="jessa"
print(nested_student_dict)'''
#10: Initialize dictionary with default values
'''employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
res=dict.fromkeys(employees,defaults)
print(res)'''
#11: Create a dictionary by extracting the keys from a given dictionary
'''sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
keys = ["name", "salary"]
new_dict={k: sample_dict[k] for k in keys}
print(new_dict)'''
#12: Delete a list of keys from a dictionary
'''sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keys = ["name", "salary"]
for k in keys:
    sample_dict.pop(k)
print(sample_dict)'''
#13: Check if a value exists in a dictionary
'''sample_dict = {'a': 100, 'b': 200, 'c': 300}
key=int(input("enter value to check:"))
if key in sample_dict.values():
    print(f"{key} present in dictionary value")
else:
    print(f"{key} is not present in dictionary values")'''
#14: Rename key of a dictionary
'''sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sample_dict['location']=sample_dict.pop('city')
print(sample_dict)'''
#15: Get the key of a minimum value
'''sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75}
print(min(sample_dict,key=sample_dict.get))'''
#16:Write a Python program to change Brad’s salary to 8500 in the following dictionary.
'''sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict['emp3']['salary']=8500
print(sample_dict)'''
#17: Invert Dictionary
'''original_dict1 = {'a': 1, 'b': 2, 'c': 3}
inverted_dict={}
for key,value in original_dict1.items():
    inverted_dict[value]=key
print(inverted_dict)'''
# 18: Sort Dictionary by Keys
'''my_dict = {'apple': 3, 'zebra': 1, 'banana': 2, 'cat': 4}
print(sorted(my_dict.items()))'''
#19: Sort Dictionary by Values
my_dict = {'Jessa': 3, 'Kelly': 1, 'Jon': 2, 'Kerry': 4, 'Joy': 1}
print(sorted(my_dict.keys()))
