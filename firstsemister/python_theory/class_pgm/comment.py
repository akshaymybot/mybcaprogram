#process a single students data 
#name,roll,mobile,email
#5sub mark,total,using nested list
n=[]
r=[]
m=[]
e=[]
print("-------student details--------")
marks=[]
total=0
name=(input("enter the name :"))
roll=int(input("enter the roll no:"))
mob=int(input("enter your mobile no: "))
email=input("enter ur email:")
for i in range(5):
    newmark=int(input("enter the subject mark:"))
    marks.append(newmark)
    n.append(name)
    r.append(roll)
    m.append(mob)
    e.append(email)
    student_data=[name,roll,mob,email,marks]
for i in range(len(marks)):
    total+=marks[i]
print("the student details and total marks is :",[student_data,total])


    


    
