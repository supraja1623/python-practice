import random,string
letters=list(string.ascii_letters)
numbers=list(string.digits)
symbols=list(string.punctuation)
print("welcome to password generator!")
n_letters=int(input("how many letters would  you like to have in your password:"))
n_numbers=int(input("how many numbers would  you like to have in your password:"))
n_symbols=int(input("how many symbols would  you like to have in your password:"))
password_list=[]
for i in range(n_letters):
    password_list.append(random.choice(letters))
for i in range(n_numbers):
    password_list.append(random.choice(numbers))
for i in range(n_symbols):
    password_list.append(random.choice(symbols))
    random.shuffle(password_list)
password=''.join(password_list)
print("your password is:")
print(password)
print("your password has been generated successfully!")