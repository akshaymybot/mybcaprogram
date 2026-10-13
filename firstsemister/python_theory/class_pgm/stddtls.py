sub1=0
sub2=0
sub3=0
total=0
avg=0
pers=0
name=""
roll=0
def std_details():
 global name,sub1,sub2,sub3,roll
 name=str(input("enter your name"))
 roll=int(input("enter your roll no"))
 sub1=int(input("enter sub1 mark"))
 sub2=int(input("enter sub2 mark"))
 sub3=int(input("enter sub3 mark"))
def total_marks():
  global total,sub1,sub2,sub3
  total=sub1+sub2+sub3
  return total
def avg_mark():
  global avg,total
  avg=total/3
  print("average is %d",avg)
def persentage_std():
  global total,pers
  pers=total/300*100
  print("persantage is %d",pers)
total_marks()