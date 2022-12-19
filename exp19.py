n=int(input("Enter the value:"))
n1=0
n2=1
count=0
print("Fibonacci series")
while(count<n):
  print(n1)
  N=n1+n2
  n1=n2
  n2=N
  count=count+1