

balance=1500
name=str (input("name:"))
pan_no=int(input("enter your pan number:"))
accno=int(input("enter your account number:"))
dob=input("enter your date of birth:")
email=input("email:")
address=str(input("enter your address(place):"))
cont=str(input("enter yourcontry:"))
new_balance=int(input("enter the new balance:"))
tupledata=(accno,name,pan_no,dob)
listdata=(email,address,cont,balance)
bank_details=[tupledata,listdata]
current_bal=balance=new_balance
bank_details[4]=current_bal
print(bank_details[4])