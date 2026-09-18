#to find if an element is in a list or not
marks=[1,2,3,4,5]
if 2 in marks:
    print("Yes")
else:
    print("No")
if "Aa" in "Aaryan":
    print("yes")
print(marks[:]) #output: [1, 2, 3, 4, 5]
print(marks[1:4]) #output: [2, 3, 4]
print(marks[1:4:2]) #output: [2, 4]
lst=[i for i in range(1,11)]
print(lst) #output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst=[i for i in range(1,11) if i%2==0]
print(lst) #output: [2, 4, 6, 8, 10]
lst=[i*i for i in range(1,11)]
print(lst) #output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]