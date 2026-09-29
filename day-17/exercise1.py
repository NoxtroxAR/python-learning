#who wants to be a millionare
opt=0
Actualans=None
qn=["What is the largest mountain?","Who is the prime minister of nepal?","What is aaryans fav color?"]
optionA=["Kanchanjanga","Sudan","Blue"]
optionB=["Everest","kp","Red"]
optionC=["K2","Deuba","orange"]
optionD=["Macchapichere","Balen","Green"]
Ans=["Everest","Balen","Blue"]
points=0
print("Welcome to who wants to be a millionare")
for i in range(len(qn)):
    print(f"{i+1}.{qn[i]}")
    print(f"1.{optionA[i]}   2.{optionB[i]}")
    print(f"3.{optionC[i]}   4.{optionD[i]}")
    opt=int(input("Enter a option from 1-4= "))
    if(opt==1):
        Actualans=optionA[i]
    elif(opt==2):
        Actualans=optionB[i]
    elif(opt==3):
            Actualans=optionC[i]
    elif(opt==4):
            Actualans=optionD[i]
    else:
          print("Invalid input")
    if Actualans==Ans[i]:
          print("Correct Answer")
          points+=1
    else:
          print("Wrong answer")
          print(f"The correct ans is {Ans[i]}")
print("---------The game has Finished------")
print(f"You end up with {points} points")