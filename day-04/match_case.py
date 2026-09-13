x=int(input('Enter a value'))
match x:
    case 0:
        print("It is zero")
    case 5:
        print("It is 5")
    case _ if x<10:
        print("x is less than 10")
    case _ :
        print("x is greater than 10")