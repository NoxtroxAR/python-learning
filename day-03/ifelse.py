#If-else statement
if 5 > 2:
    print("Five is greater than two!")
    age=int(input("Enter your age: "))
if age < 18:
        print("You are a minor.")
elif age == 18:
        print("You are exactly 18 years old.")
elif age>100:
        print("You are over 100 years old.")
else:
         print("You are an adult.")
#Conditonal statements can be used to control the flow of a program based on certain conditions. In this example, we first check if 5 is greater than 2, which is true, so we print a message. Then, we ask the user to input their age and check if they are a minor or an adult based on the input.
#ex: > < >= <= == !=
#nested if-else
if 5 > 2:
    print("Five is greater than two!")
    age=int(input("Enter your age: "))
    if age < 18:
        print("You are a minor.")
    elif age == 18:
        print("You are exactly 18 years old.")
    elif age>100:
        print("You are over 100 years old.")
    else:
         print("You are an adult.")

    if(2%2==0):
        print("2 is even")
    else:
        print("2 is odd")