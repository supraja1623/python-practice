#1:Write a code to create a new list using odd-indexed elements from the first list and even-indexed elements from the second
'''l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
oddindex=l1[1::2]
print("odd index in first list is:",oddindex)
evenindex=l2[::2]
print("even index in second list is:",evenindex)
print("final list is",oddindex+evenindex)'''
#2:Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.
'''list1 = [54, 44, 27, 79, 91, 41]
res=list1.pop(4)
print("after removing element at 4th index:",list1)
element=list1.insert(2,23)
print("after adding element at 2nd index:",list1)
add=list1.append(16)
print("after adding number in the list is:",list1)'''
#3: Slice list into 3 equal chunks and reverse each chunk
'''sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
chunk1=sample_list[0:3]
print("chunk 1 :",chunk1)
print("after reversing chunk 1:",chunk1[::-1])
chunk2=sample_list[3:6]
print("chunk 2:",chunk2)
print("after reversing chunk 2:",chunk2[::-1])
chunk3=sample_list[6::]
print("chunk 3:",chunk3)
print("after reversing chunk 3:",chunk3[::-1])'''
#4: Count the occurrence of each element from a list
'''sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
count_dict=dict()
for item in sample_list:
    if item in count_dict:
        count_dict[item]+=1
    else:
        count_dict[item]=1
print("printing count of each item:",count_dict)'''
#5: Paired Elements from Two Lists as a Set
'''first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
print(set(zip(first_list,second_list)))'''
#6: Set Intersection and Removal
'''first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
result=first_set.intersection(second_set)
print("common elements from two sets is:",result)
for item in result:
    first_set.remove(item)
print("first set after removing common element:",first_set)'''
#7: Subset or Superset of another set
'''first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}
print("first set is subset of second set:",first_set.issubset(second_set))
print("second set is subset of first set :",second_set.issubset(first_set))
print("First set is Super set of second set - ", first_set.issuperset(second_set))
print("Second set is Super set of First set - ", second_set.issuperset(first_set))
if first_set.issubset(second_set):
    first_set.clear()
if second_set.issubset(first_set):
    second_set.clear()
print("first set is:",first_set)
print("second set is:",second_set)'''
#10: remove duplicates from a list
'''sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
print("after deleting duplicates:",set(sample_list))
t=tuple(sample_list)
print("maximum element in tuple is:",max(t))
print("minimum elemnt in tuple is:",min(t))'''
