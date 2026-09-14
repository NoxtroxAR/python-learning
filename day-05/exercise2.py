#check if prime
n=int(input("Enter a number: "))
check=True
if(n<2):
    check=False
else:
    for i in range(2,n):
        if(n%i==0):
            check=False
            break
if(check==True):
    print(n," is a prime number")
else:
    print(n," is not a prime number")