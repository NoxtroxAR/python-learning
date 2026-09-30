#short hand if else statement also known as ternary operator is used to check condition on a single sentenece
age=17
status="adult" if age>=18 else "Child"
print(status)
print("Hello") if age>=18 else print("hoala") 
#the function enumerate will give index
marks=[1,2,67,89]
for index,mark in enumerate(marks,start=1):#start=1 is not necceesary the defualt start is 0 if u dont add that
    print(index,mark)
'''
Vietual enviromnet
By default,
 when you install Python packages on your computer, they all go into one giant global folder.
 If Project A needs version 1.0 of a library, but Project B needs version 2.0 of that exact same library,
your global setup breaks because they conflict.
 A virtual environment solves this by giving every project its own private folder containing its own Python executable and installed packages.
'''