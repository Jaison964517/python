class Bank:
    def __init__(self ,a,n,t,b):
        self.A=a
        self.name=n
        self.type=t
        self.balance=b

    def printacc(self):
        # print(self.A,self.name,self.type,self.balance)
        print("ACC No:",self.A)
        print("ACC NAME:", self.name)
        print("ACC Type:", self.type)
        print("Balance:", self.balance)
    def depo(self, a1):
        self.balance += a1
        print("Balance:", self.balance)
    def withdrw(self,c1):
        if self.balance<c1:
         print("invalid")
        else:
          self.balance-=c1
          print("Balance",self.balance)




a=int(input("enter acc no:"))
n=input("enter name:")
t=input("eneter acc type:")
b=int(input("BALANCE:"))
b1=Bank(a,n,t,b)
b1.printacc()
a1=int(input("enter the amount depo:"))
b1.depo(a1)
c1=int(input("enter the amount withdrw:"))
b1.withdrw(c1)


