#1: Perform Basic Set Operations
'''fruits = {"apple", "banana", "mango", "orange"}
print("1. After creating the set:", fruits)
fruits.add("grape")
print("2.after adding grape to the set:",fruits)
fruits.remove("banana")
print("3.after removing banana from set:",fruits)
fruits.discard("mango")
print("4.after discarding mango the set will be:",fruits)'''
# 2: Union of Sets
'''set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.union(set2))'''
#3: Intersection of Sets
'''set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))'''
#4: Difference of Sets
'''set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.difference(set2))'''
#5: Symmetric Difference
'''set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.symmetric_difference(set2))'''
#6: Add a list of Elements to a Set
'''sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
sample_set.update(sample_list)
print(sample_set)'''
#7: Set Difference Update
'''set1 = {10, 20, 30}
set2 = {20, 40, 50}
print(set1.difference(set2))'''
#8: Remove Items From Set Simultaneously
'''set1 = {10, 20, 30, 40, 50}
print(set1.difference({10,20,30}))'''
#9: Check Subset
'''subset_set = {10, 20}
main_set = {10, 20, 30, 40}
print(main_set.issubset(subset_set))'''
#10: Check Superset
'''set1 = {10, 20}
set2 = {10, 20, 30, 40}
print(set2.issuperset(set1))'''
#11: Set Intersection Check
'''set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
print(set1.intersection(set2))'''
#12: Set Symmetric Difference Update
'''set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.symmetric_difference(set2))'''
# 13: Set Intersection Update
'''set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection_update(set2)
print(set1)'''
#14: Find Common Elements in Two Lists
'''list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]
set1=set(list1)
set2=set(list2)
print(set1.intersection(set2))'''
#15: Frozen Set
'''my_list = [10, 20, 30]
print(frozenset(my_list))'''
#16: Count Unique Words
'''sentence= "dog is a simple animal dogs is selfless animal"
words=sentence.lower().split()
unique=set(words)
length=len(unique)
print(unique,length)'''
