#1: Print first 10 natural numbers using while loop
'''i=1
while i<=10:
    print(i,end=" ")
    i=i+1'''
#2.Write a Python code to print the following number pattern using a loop.
#1=i 
#1 2 
#1 2 3 
#1 2 3 4 
#1 2 3 4 5=j
'''row=int(input("enter a row:"))
for i in range(1,row+1,1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\t")'''
#3: Calculate sum of all numbers from 1 to a given number
'''sum=0
num=int(input("enter a number:"))
for i in range(1,num+1,1):
    sum=sum+i
print(sum)'''
#4: Print multiplication table of a given number
'''num=int(input("enter number for multiplication table:"))
for j in range(1,11):
    print(f"{num}*{j}={num*j}")
    print(end='')
print("\t")'''
# 5: Display numbers from a list using a loop
'''numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    print(i)'''
#6: Count the total number of digits in a number
'''num=int(input("enter a number:"))
number=str(num)
print(len(number))'''
#7.Write a Python program to print the reverse number pattern using a for loop.
'''num=int(input("enter a number"))
number=str(num)
print(len(number))'''
 #8: Print list in reverse order using a loop
'''list1 = [10, 20, 30, 40, 50]
reverse=list1[::-1]
print(reverse)'''
#9: Display numbers from -10 to -1 using for loop
'''for i in range(-10,0,1):
    print(i,end=" ")'''
#10: Display a message “Done” after the successful execution of the for loop
'''for i in range(5):
    print(i,end=" ")
print("\ndone!")'''
#11: Print all prime numbers within a range
'''start=25
end=50
for i in range(start,end+1):
    if i>1:
        for num in range (2,i):
            if i%num==0:
                break
        else:
            print(i)'''
#12: Display Fibonacci series up to 10 terms
'''num1,num2=0,1
for i in range(10):
    print(num1,end=" ")
    res=num1+num2
    num1=num2 
    num2=res'''
#13: Find the factorial of a given number
'''def fact(num):
    for i in range(num+1):
        if num==0 or num==1:
            return 1
        else:
            return num*fact(num-1)
print(fact(5))'''
#(or)
'''num=int(input("enter a number:"))
fact=1
if num<=0:
    print("invalid number")
else:
    for i in range(1,num+1):
        fact=fact*i
    print(fact)'''
#14: Reverse a integer number
'''num=int(input("enter a number:"))
reverse_num=0
while num>0:
    remainder=num%10
    reverse_num=(reverse_num*10)+remainder
    num=num//10
print(reverse_num)'''
#15: Print elements from a given list present at odd index positions
"""my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(my_list[1::2])"""
#16. Calculate the cube of all numbers from 1 to a given number
'''num=int(input("enter a number:"))
for i in range(1,num+1):
    res=(i**3)
    i=i+1
    print(res)'''
#17: Find the sum of a series of a number up to n terms
'''terms=5
num=2
sum_seq=0
for i in range(0,terms):
    print(num,end="+")
    sum_seq+=num
    num=num*10+2
print(sum_seq)'''
#18:Write a program to print the following start pattern using the for loop
#* 
#* * 
#* * * 
#* * * * 
#* * * * * 
#* * * * 
#* * * 
#* * 
#*

'''rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
'''
#19: Print Full Multiplication Table
'''or i in range(1,11):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")
    print("\t")'''
#22: Find largest and smallest digit in a number
'''num=int(input("enter number:"))
number=str(num)
print("maximum number is:",max(number))
print("minimum number is:",min(number))'''
#20: Print the alternate numbers pattern
#1  
#2 3  
#4 5 6  
#7 8 9 10  
#11 12 13 14 15
n = 5  # number of rows
current = 1

for i in range(1, n + 1):
    for j in range(i):
        print(current, end=" ")
        current += 1
    print()
