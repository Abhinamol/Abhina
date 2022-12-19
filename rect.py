class rectangle:
    def __init__(self,l,w):
        self.__l=l
        self.__w=w
    def area(self):
        self.__area=self.__l+self.__w
        print("Area is:",self.__area)
    def __lt__(self,other):
        if(self.__area<other.__area):
            return True
        else:
            return False
l1=int(input("Enter the length of first rectangle:"))
w1=int(input("Enter the width of first rectangle: "))
l2=int(input("Enter the length of second rectangle: "))
w2=int(input("Enter the width of second rectangle: "))
o1=rectangle(l1,w1)
o2=rectangle(l2,w2)
o1.area()
o2.area()
if o1<o2:
    print("Rectangle two is large")

else:
    print("Rectangle one is large or two rectangle is equal")