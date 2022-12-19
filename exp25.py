n1=int(input("Enter first number:"))
n2=int(input("Enter the second number:"))
gcd=1
for i in range(1,min(n1,n2)):
    if n1%i==0 and n2%i==0:
        gcd=i
print("GCD of two numbers is",gcd)