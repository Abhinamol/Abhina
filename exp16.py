m=int(input("Enter the number of elements:"))
list=[]
print("Enter the elements:")
for i in range(0,m):
    ele=int(input())
    if(ele>100):
        list.append("over")
    else:
        list.append(ele)
print(list)