n=int(input("Enter the size of list:"))
print("Enter the elements:")
list=[]
for i in range(0,n):
    ele=int(input())
    if(ele%2!=0):
        list.append(ele)
print("The list without even numbers are:",list)