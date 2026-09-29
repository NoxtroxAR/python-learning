#exception handling
#code inside "finally" will always run no matter what
a=input("Enter a number: ")
print(f"Multiplication table of {a} is: ")
try:
    for i in range(1,6):
        print(f"{int(a)}x{i}={int(a)*i}")
except Exception as e:#except:
    print(e)          #print("Invalid input") you can write like this as well
finally:
    print("i am always executed")
#qn arises saying why use a finnally block any code down of try except wil be executed but the ans is when used in a function with return type any cpde down wont be executred so u use finnaly
print("Imp lines of code")
#another example
try:
    b=int(input("Enter a number: "))
    c=[2,4]
    print(c[b])
except ValueError:
    print("Num is not integer")
except IndexError:
    print("Invalid index")