#in python we can raise custom error using the raise keyword
#first qn
try:
    n=int(input("Enter the amount of subjects: "))
    a=[]
    for i in range(n):
        m=int(input("Enter marks: "))
        if(m<0 or m>100):
            raise ValueError("Marks greater than 100 or less than 0")
        a.append(m)
except ValueError as e:
    print(e)
finally:
    print("Hi")
for i in range(n):
    print(a[i])
'''
a=int(input("Enter a num between 1-5: "))
if(a<1 or a>5):
    raise ValueError("Invalid int input")'''