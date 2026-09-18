def check_g(func_item):
    for i in range(5):
        a=func_item[0]
        for i in range(5):
            if(a<func_item[i]):
                a=func_item[i]
    return a
def check_s(func_item):
    for i in range(5):
        a=func_item[0]
        for i in range(5):
            if(a>func_item[i]):
                a=func_item[i]
    return a
item=[]
for i in range(5):
    n=int(input("Enter numbers:"))
    item.append(n)
print("The greatest element is: ",check_g(item))
print("The smallest element is: ",check_s(item))
