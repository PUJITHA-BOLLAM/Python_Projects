class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.marks={}
    def mark(self):
        keys=["Telugu","Hindi","English","Maths","Science","Social"]
        for i in range(len(keys)):
            print("Enter your marks in ",keys[i])
            k=int(input(""))
            self.marks[keys[i]]=k
    def sum_marks(self):
        s=0
        for i in self.marks.values():
            s+=i
        return s
    def avg(self):
        s=0
        for i in self.marks.values():
            s+=i
        a=s/len(self.marks)
        return a
    def grade(self):
        a=self.avg()
        if(a>90 and a<=100):
            return 'A'
        elif(a>80 and a<=90):
            return 'B'
        elif(a>70 and a<=80):
            return 'C'
        elif(a>60 and a<=70):
            return 'D'
        else:
            return 'F'
    def pass_or_fail(self):
        if(self.grade()=='F'):
          return "Fail"
        else:
            return "Pass"
    def display(self):
        self.mark()
        print("------- Report Card -------")
        print("Name: ",self.name)
        print("Roll No: ",self.roll)
        print("Marks:\n")
        for sub,mark in self.marks.items():
            print(sub," : ",mark)
        print("Sum of marks:",self.sum_marks())
        print("Average:",self.avg())
        print("Grade:",self.grade())
        print("Pass or Fail:",self.pass_or_fail())
        
n=input("Enter student name")
m=int(input("Enter student roll no"))
s=Student(n,m)
s.display()
k=School(s)
