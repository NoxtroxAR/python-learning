item=[]
even=[]
odd=[]
n=int(input("Enter a number: "))
for i in range(n):
    a=int(input("Enter item:"))
    item.append(a)
print(item)
for i in range(n):
    if (item[i]%2==0):
        even.append(item[i])
    else:
        odd.append(item[i])
print(even)
print(odd)