my_task=[]
while(True):
    print("Menu")
    print("1.Add Tasks")
    print("2.View Tasks")
    print("3.Exit")
    k=int(input("Enter your choice"))
    if(k==1):
        task=input("Enter the task")
        my_task.append(task)
        print("Task added successfully")
    elif(k==2):
        if(my_task==[]):
            print("No tasks yet")
        else:
            print("---Tasks---")
            for i in enumerate(my_task,start=1):
                 print(i)
    elif(k==3):
        print("Exiting...")
        break
    else:
        print("Invalid choice")


