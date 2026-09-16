#default argumnet
def calculate(a, b=0):
    print(a+b)
calculate(10, 20) #output: 30
calculate(10) #output: 10
#ordered argumnet:Order doesnt matter in keyword arguments
calculate(b=20, a=10) #output: 30
#required argument: If a function has a required argument, it must be passed in the function call. If not, it will raise an error.
def calculate_required(a, b):
    print(a+b)
calculate_required(10, 20) #output: 30
# calculate_required(10) # This would raise a TypeError since 'b' is a required argument.

#variable length argument: A variable-length argument allows you to pass a variable number of arguments to a function. In Python, you can use *args for non-keyword variable-length arguments and **kwargs for keyword variable-length arguments.
def calculate_variable_length(*args):
    total = sum(args)
    print(total)
calculate_variable_length(10, 20, 30) #output: 60
def average(*n):
    for i in n:
        print(i)
average(1,2,3,4,5) #output: 1 2 3 4 5
