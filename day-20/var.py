#local variable are those variable made inside a function and can be only used inside that function
#global variable are those variable made outside a function and can be used anywhere in the program
x=4#global variable
y=3
def myf():
    x=5#local variable
    global y#this says that use the global variable y instead of creating a new local variable y
    y=6#this will modify the global variable y
    print(f"The local x is {x}")
    print(f"The local y is {y}")
print(f"The global x is {x}")
print(f"The global y is {y}")
myf()
print(f"The global x is {x}")
print(f"The global y is {y}")