#1.calculate the sum and multiplication of two numbers
''''a=int(input("enter first  number:"))
b=int(input("enter second number:"))
print("sum is:",a+b ,"and multiplication is:",a*b)'''

#2: Print the Sum of a Current Number and a Previous number
'''prev_number=0
for i in range(0,11):
    print(f"previous number is {prev_number} and current number is {i} their sum is {prev_number+i}")
    prev_number=i'''

#3: Print characters present at an even index number
'''string=input("enter a string:")
size=len(string)
for i in range(0,size-1,2):
    print(string[i],end=" ")'''

 #4: Remove first n characters from a string
'''def remove_chars(word,n):
    x=word[n:]
    return x
print(remove_chars("pynative",2))'''
#5: Check if the first and last numbers of a list are the same
'''numbers_x = [10, 20, 30, 40, 10]
first_num=numbers_x[0]
last_number=numbers_x[-1]
if first_num==last_number:
    print("first and last numbers are equal")
else:
    print("first and last numbers are not equal")
'''
#Display numbers divisible by 5
'''ist_1=[10, 20, 33, 46, 55]
for i in list_1:
    if i%5==0:
        print(i,end=" ")'''

#7: Find the number of occurrences of a substring in a string
'''str_x="Emma is good developer. Emma is a writer"
cnt=str_x.count("Emma")
print(cnt)'''
#8: Print the following pattern
#1 
#2 2 
#3 3 3 
#4 4 4 4 
#5 5 5 5 5
'''for num in range(10):
    for i in range(num):
        print(num,end=" ")
    print("\n")'''
#9: Check Palindrome Number
'''num=int(input("enter a number:"))
num1=str(num)
first=num1[0]
last=num1[-1]
if first==last:
    print(f"yes, {num} is palindrome.")
else:
    print(f"no,{num} is not a palindrome.")'''
#10.Given two lists of numbers, write Python code to create a new list containing odd numbers from the first list and even numbers from the second list.
'''list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
my_list=[]
for i in list1:
    if i%2!=0:
        my_list.append(i)
for j in list2:
    if j%2==0:
        my_list.append(j)
print(my_list)'''
#11.Get each digit from a number in the reverse order.
'''
number = 7536
num=str(number)
print(num[::-1])'''

#12: Print multiplication table from 1 to 10
'''for i in range(1,11):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")
        print(end=" ")'''
#13: Print a downward half-pyramid pattern of stars
#* * * * *  
#* * * *  
#* * *  
#* *  
#*
'''for i in range(6,0,-1):
    for j in range(0,i-1):
        print("*",end=' ')
    print(" ")'''
#14.Get an int value of base raises to the power of exponent
'''def expobase(base,exponent):
    return base**exponent
print(int(expobase(2,3.5)))'''

#15: Generate Fibonacci series up to 15 terms
'''num1,num2=0,1
for i in range(15):
    print(num1,end=" ")
    result=num1+num2
    num1=num2
    num2=result'''

#16: Check if a given year is a leap year
'''year=int(input("enter a year:"))
if (year%4==0 and year%100!=0) or year%400==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")'''


