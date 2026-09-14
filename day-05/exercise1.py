#number analyzer,Print number frim 1 to n
n=int(input("Enter a number: "))
even_count=0
odd_count=0
sum_e=0
sum_o=0
for i in range(1,n+1):
    print(i)
    if(i%2==0):
        even_count+=1
        sum_e+=i
    else:
        odd_count+=1
        sum_o+=i
print("No of even number is: ",even_count)
print("No of odd number is: ",odd_count)
print("Sum of even number is:",sum_e)
print("Sum of odd number is:",sum_o)