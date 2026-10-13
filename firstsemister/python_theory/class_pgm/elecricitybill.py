unit=int(input("how many units used :"))
category=int(input("enter the type of category-->\n1=non commercial\n2=commercial\n--> :"))
threshold=int(input("yes=1\nno=0\n-->  :"))
amount=1
if unit<=100 and category==1 and threshold==0:
    amount=unit*5
if unit<=100 and category==1 and threshold==1:
    amount=unit*5+50
if unit<=100 and category==2 and threshold==0:
    amount=unit*10
if unit<=100 and category==2 and threshold==1:
    amount=unit*10+100
if 100<unit<=300 and category==1 and threshold==0:
    amount=(unit-100)*6+(100*5)
if 100<unit<=300 and category==1 and threshold==1:
    amount=(unit-100)*6+(100*5)+50
if 100<unit<=300 and category==2 and threshold==0:
    amount=(unit-100)*12+(100*10)
if 100<unit<=300 and category==2 and threshold==1:
    amount=(unit-100)*12+(100*10)+100
if unit >300 and category==1 and threshold==0:
    amount=(unit-300)*8+(200*6)+(100*5)
if unit >300 and category==1 and threshold==1:
    amount=(unit-300)*8+(200*6)+(100*5)+50
if unit >300 and category==2 and threshold==0:
    amount=(unit-300)*15+(200*12)+(100*10)
if unit >300 and category==2 and threshold==1:
    amount=(unit-300)*15+(200*12)+(100*10)+100
print("the amount to be paid :",amount,"rs")
