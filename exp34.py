class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return(self.length*self.breadth)
    def perimeter(self):
        return(2*(self.length+self.breadth))
l=int(input("Enter the length of first rectangle:"))
b=int(input("Enter the breadth of second rectangle:"))
x=rectangle(l,b)
y=x.area()
z=x.perimeter()
print("Area of first rectangle is",y)
print("perimeter of first rectangle  is",z)
l1=int(input("Enter the length of second rectangle:"))
b1=int(input("Enter the breadth of second rectanle:"))
x1=rectangle(l1,b1)
y1=x1.area()
z1=x1.perimeter()
print("Area  of second rectangle is",y1)
print("perimeter of second rectangle is",z1)

if(y>y1):
    print("first rectangle is greater the second rectangle")
else:
    print("second rectangle is greater the first rectangle")


