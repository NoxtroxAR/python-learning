#reverse of a number
rev=0
n=int(input("Enter a number: "))
while(n!=0):
    rev=rev*10+(n%10)
    n//=10
print("The reverse of the number is ",rev)