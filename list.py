#Perform following operations on given list
# 1.access Elements: Print the third element.
#2.List Length: Print the number of elements in the list
#3.Check if Empty: Write a code to check is list empty
'''my_list = [10, 20, 30, 40, 50]
print("initial list:",my_list)
print("third element is:",my_list[2])
length=len(my_list)
print("length of the list is:",length)
if length==0:
    print("list is empty.")
else:
    print("list is not empty")'''
#2.Perform following list manipulation operations on given list
#1.Change Element: Change the second element of a list to 200 and print the updated list.
#2.Append Element: Add 600 to the end of a list and print the new list.
#3.Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
#4.Remove Element (by value): Remove 600 from the list and print the list.
#5.Remove Element (by index): Remove the element at index 0 from the list print the list.
'''my_list = [10, 20, 30, 40, 50]
print("initial list:",my_list)
my_list[1]=200
print("after changing 2nd element in the list the updated list is:",my_list)
my_list.append(600)
print("after adding 600 at the end of the list is:",my_list)
my_list.insert(2,300)
print("after inserrting 300 at the third position:",my_list)
my_list.remove(600)
print("after removing 600 the updated list is:",my_list)
my_list.pop(0)
print("after delting zero index the updated list is:",my_list)'''
#3: Sum and average of all numbers in a list
'''my_list = [10, 20, 30, 40, 50]
sum=0
for i in my_list:
    sum+=i
average=sum/len(my_list)
print(f"sum of the list is {sum} and average is {average}")'''
#Exercise 4: Reverse a list
'''list1 = [100, 200, 300, 400, 500]
print("reversed list is:",list1[::-1])'''
# 5: Turn every item of a list into its square
#numbers = [1, 2, 3, 4, 5, 6, 7]
'''res=[]
for i in numbers:
    res.append(i*i)
print(res)'''
#or
'''res=[x*x for x in numbers]
print(res)'''

#6:Find and print the largest and smallest number in a list [8, 2, 15, 1, 9].
'''data=[8, 2, 15, 1, 9]
print("maximum element is:",max(data))
print("minimum element in the list is:",min(data))'''
#7:Count and print how many times 'Football' appears in list.
'''sports = ['Cricket', 'Football', 'Hockey', 'Football', 'Tennis']
print(sports.count('Football'))'''
#8: Sort a list of numbers
'''numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers)'''
#9: Create a copy of a list
'''data=[10, 20, 30]
print(data.copy())'''
#10: Combine two lists
'''list_a = [1, 2]
list_b = [3, 4]
print(list_a+list_b)'''
#11: Remove empty strings from the list of strings
'''list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print(list(filter(None,list1)))'''
#12: Remove Duplicates from list
'''list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]
print(set(list_with_duplicates))'''
#13: Remove all occurrences of a specific item from a list
'''list1 = [5, 20, 15, 20, 25, 50, 20]
while 20 in list1:
    list1.remove(20)
print(list1)'''
#14: List Comprehension for Numbers
'''my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]
list1=[ item for item in my_list if isinstance(item,(int,float)) ]
print(list1)'''
#15: Access Nested Lists
'''nested_list = [[10, 20, 30], [44, 55, 66], [77, 87, 99]]
element=nested_list[1][1]
print(element)'''
#16: Flatten Nested List
#list_of_lists = [[1, 2], [3, 4], [5, 6, 7]]
#pending
# 17: Concatenate two lists index-wise
'''list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3=[i+j for i,j in zip(list1,list2)]
print(list3)'''
#18: Concatenate two lists in the following order
'''list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3=[x+y for x in list1 for y in list2]
print(list3)'''
#19: Iterate both lists simultaneously
'''list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x,y in zip(list1,list2[::-1]):
    print(x,y)'''
#21: Add new item to list after a specified item
'''list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)'''
#22.You have given a nested list. Write a program to extend it by adding the sublist ["h", "i", "j"] in such a way that it will look like the following list.
'''list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print(list1)'''
#23:You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.
'''list1 = [5, 10, 15, 20, 25, 50, 20]
index=list1.index(20)
list1[index]=200
print(list1)'''

