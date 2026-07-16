total=0
while(True):
    print("\n1.Add Expense\n2.View Total Spent\n3.Quit")
    k=int(input("Enter your choice"))
    if(k==1):
       try:
         e=input("Enter your expense")
         total+=int(e)
         print("Expense Added Successfully")
       except ValueError:
           print("Invalid Data")       
    elif(k==2):
        print("Total Spent: ",total)
    elif(k==3):
        print("Quiting..")
        break
    else:
        print("Invalid choice")
    
