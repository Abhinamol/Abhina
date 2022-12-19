s=int(input("Enter the number of strings:"))
list=[]
count=0
print("Enter the strings:")
for i in range(0,s):
    str=input()
    list.append(str)
print(list)
for i in list:
    for j in i:
        if(j=="a"):
            count=count+1
print("Number of occurence of 'a':",count)