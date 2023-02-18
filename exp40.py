f=open("demo.txt.txt","r")
f2=open("odd.txt","w")
content=f.readlines()
for i in range(0,len(content)):
    if(i%2!=0):
        f2.write(content[i])
    else:
        pass
f.close()
f2.close()
f=open("odd.txt","r")
e=f.read()
print("Odd lines are:",e)
f.close()