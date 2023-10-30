fyear=int(input("enter the first year:"))
Lyear=int(input("enter the last year:"))
for i in range(fyear,Lyear):
  if((i%4==0)and(i%100!=0)or(i%400==0)):
      print(i)

