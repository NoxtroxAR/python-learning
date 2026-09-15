#Sum of digits
digits=0
sum=0
n=int(input("Enter a number: "))
while(n!=0):
    digits=n%10
    sum+=digits
    n//=10
print("Sum of digits is: ",sum)