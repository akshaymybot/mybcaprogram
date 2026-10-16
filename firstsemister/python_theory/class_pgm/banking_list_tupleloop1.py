def inpot():
    my_list=[]
    tup=()
    accountnumber=int(input("enter your act n umber:"))
    pannum=input("enter the pan:")
    name=input("enter the name: ")
    dob=input("enter ur dob:")
    tup=(accountnumber,name,pannum,dob)
    my_list.append(tup)
    adress=input("enter ur adress:")
    my_list.append(adress)
    email=input("enter ur email:")
    my_list.append(email)
    mobli=int(input("enter ur number:"))
    my_list.append(mobli)
    balance=500
    my_list.append(balance)
    return my_list
    
def display(my_list):
    print("your act number is ",my_list[0][0])
    print("your act pan-num   is ",my_list[0][1])
    print("your name  is ",my_list[0][2])
    print("your date of birth is ",my_list[0][3])
    print("your adress is ",my_list[1])
    print("your email is ",my_list[2])
    print("your moble numbr is  is ",my_list[3])

    print("YOUR ACT BALANCE ---------> ",my_list[4])
def withdraw(my_list):
    amount=int(input("\nenter the amount to withdraw\n"))
    my_list[4]=my_list[4]-amount
    print("your balance=",my_list[4])
    return my_list
def depo(my_list):
    amount=int(input("\nenter the amount to deposite\n"))
    my_list[4]=my_list[4]+amount
    print("your balance=",my_list[4])
    return my_list
n=int(input("enter number of act "))
mainlist=[]
for i in range(n):
    print(f"ACT {i+1} details ")
    my_list=inpot()
    a=0   
    mainlist.append(my_list)
print("",mainlist)
end=0
while end==0:
    for J in range(n):
        act=int(input("enter your act number "))
        if act==mainlist[J][0][0]:
            print("your details",mainlist[J][0])
            ch=0
            while ch!=3:
                ch=int(input("enter ur choice 1=diplay 2=witdraw 3=deposite 4=exit "))
                if ch==1:
                    display(mainlist[J])
                elif ch==2:
                    withdraw(mainlist[J])    
                elif ch==3:
                    depo(mainlist[J])
                elif ch==4:
                    end=1
                else:
                    print("enter valid choice")
                                    

            break;     
        else:
            print("act not found")