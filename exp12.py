string=input("Enter the string:")
a=string[0]
for i in string:
    if(i==a):
        string=string.replace(i,'$')
        string=a+string[1:]
print(string)