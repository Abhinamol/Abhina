class bank:
    def __init__(self,accno,name,balance,type):
        self.accno=accno
        self.name=name
        self.balance=0
        self.type=type
    def showacc(self):
        print("Account number is",self.accno)
        print("User name is",self.name)
        print("Account balance is",self.balance)
        print("Account type is",self.type)
    def dep(self,d):
        self.balance=self.balance+d
        return self.balance
    def wtthd(self,w):
        self.balance=self.balance-w
        return self.balance
n=int(input("Enter the acount number"))
name=input("Enter the name")
t=input("Enter the account type")
o=bank(n,name,t)
o.showamt()
while(True):
    print("1.Deposit \n 2.Withdraw" )
    c=int(input("Enter your choice"))
    if(c==1):
        d1=int(input("Enter the amount to deposit:"))
        o.dep(d1)
        o.showamt()
    elif(c==2):
        w1=int(input("Enter the amount to be withdrawed"))
        o.wirhd(w1)

