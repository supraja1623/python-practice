todo_list=[]
while True:
    print("1.add task\n")
    print("2.view tasks\n")
    print("3.update task\n")
    print("4.delete task\n")
    print("5.exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        task=input("enter your task:")
        time=input("enter time:")
        todo_list.append((task,time))
        print("task added successfully.")
    elif choice==2:
        if len(todo_list)==0:
            print("no tasks added.")
        else:
            print("\n your todo list:")
            for i in range(len(todo_list)):
                print(i+1,".",todo_list[i][0],"-",todo_list[i][1])
    elif choice==3:
        if len(todo_list)==0:
            print("no tasks to update.")
        else:
         num=int(input("enter task number to update:"))
        if 1<=num<=len(todo_list):
                new_task=input("enter new task:")
                new_time=input("enter new time:")
                todo_list[num-1]=(new_task,new_time)
                print("task updated successfully.")
        else:
             print("invalid task number.")
    elif choice==4:
        if len(todo_list)==0:
            print("no tasks to delete")
        else:
            num=int(input("enter task number to delete:"))
            if 1<=num<=len(todo_list):
                todo_list.pop(num-1)
                print("task deleted successfully.")
            else:
                print("invalid task number.")
    elif choice==5:
        print("existing todo list")
        break       
    else:
        print("invalid choice")