clas={
    "Aaryan":1,
     "CS":"Subject"
}
clz={
    "hello":"World"
}
print(clas.keys())
clas.update(clz)
#clas.clear() clears the whole dictionaru
print(clas)
clas.pop("CS")
#clas.popitem() clears the last item
print(clas)
del clz#deltes the whole dictionary
#storing in a dic
students={}
for i in range(5):
    name=input("Enter a name: ")
    age=int(input("Enter age: "))
    students[name]=age
print(students)