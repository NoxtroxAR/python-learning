student={}
avg=0
n=int(input("Enter the no of studnets= "))
for i in range(n):
    name=input(f"Enter the name of sdtudent no {i+1}= ")
    marks=[]
    for j in range(3):
        mark=int(input(f"Enter the marks of subject {j+1}= "))
        marks.append(mark)
    student[name]=marks
for key in student.keys():
    print(f"The {key} has these set of marks={student[key]}")
    for marks in student[key]:
        avg+=marks
    act_avg=avg/len(student[key])
    print(f"The average is {act_avg}")
    if(act_avg>=90):
        print("Grade: A")
    elif(act_avg>=80):
        print("Grade B")
    else:
        print("FAIL")