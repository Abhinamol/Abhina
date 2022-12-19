class time:
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second

    def __add__(self, other):
            self_add= self.__hour + other.__hour + self.__minute + other.minute+self.second+other.second
            print("Sum is")

    def __str__(self):
            return (self.hour, self.minute,self.second)

h1=int(input("Enter the hour(1)"))
m1=int(input("Enter the minutes(1)"))
s1=int(input("Enter the seconds(1)"))
h2=int(input("Enter the hour(2)"))
m2=int(input("Enter the minutes(2)"))
s2=int(input("Enter the seconds(2)"))
o1=time(h1,m1,s1)
o2=time(h2,m2,s2)


