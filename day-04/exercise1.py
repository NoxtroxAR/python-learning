#Ask user for a password must be 8 character,must have @,must not contain a space
key=input("Enter a password:")
if(len(key)==8):
    print("There are 8 characters")
    if "@" in key:
        print("There is an @")
        if " " not in key:
            print("The password has no space")
            print("It has all the criteria fullfilled to be a strong password")
            password=key
            print("This is ",password," the password")
        else:
            print("The password has white space")
    else:
        print("There is no @")
else:
    print("There must be 8 characters")