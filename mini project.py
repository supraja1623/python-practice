dict1={}
while True:
    print("1.enter your word")
    print("2. search for meaning")
    print("3.dispaly all words")
    print("4.update meaning")
    print("5.delete word")
    print("6.exist")
    choice=int(input("enter your choice:"))
    if choice==1:
        word=input("enter your to add:").lower()
        meaning=input("enter meaning of your word:")
        dict1.update({word:meaning})
        print("your word added successfully!😊")
    elif choice==2:
        word=input("enter your to search:")
        meaning=dict1.get(word)
        if meaning:
          print(f"the meaning of a {word} is {meaning}.")
        else:
            print(f"{word} not found!")
    elif choice==3:
        if dict1:
            dict1.items()
            print(dict1)
        else:
            print("dictionary is empty.")
    elif choice==4:
        word=input("enter word to update:")
        if word in dict1:
            new = input("enter meaning of the word:")
            dict1.update({word:new})
            print("meaning updated successfully!")
        else:
            print("word no found!")
    elif choice==5:
        word=input("enter your word to delete:")
        if word in dict1:
            del dict1[word]
            print("word deleted successfully!")
        else:
            print("word not found to delete!")
    elif choice==6:
        print("👋exiting program........Goodbye!")
        break
    else:
        print("invalid choice,try again!")

      
