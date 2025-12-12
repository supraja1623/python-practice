'''rules :- 1.rock wins against scissor
2.paper wins against rock
3.scissor wins against paper
coumputer choice ==user Choice:
print("draw")
coumputer choice=0 and userchoice=2:
print(you lose)
computerchoice=2 and user choice=0:
print(you win)
computerchoice>userchoice:
print(you lose)'''

import random
user_choice=int(input("enter 0 for rock,1 for paper,2 for scissor"))
computer_choice=random.randint(0,2)
print(f"computer chosses:{computer_choice}")
if user_choice not in[0,1,2]:
    print("number does not exist")
    exit()
if computer_choice==user_choice:
    print("draw")
elif user_choice==0 and computer_choice==2:
    print("you win")
elif computer_choice==0 and user_choice==2:
    print("you lose")
elif computer_choice>user_choice:
    print("you lose")
elif user_choice>computer_choice:
    print("you win")    