#tuple is very similar to list one of the only differenve is tuple cannot be changed
tup=(1,2,3,"Hari")
print(tup)
print(tup[0])#prints the first element of tuple
#tup[0]=5#this will give an error because tuple cannot be changed
print(tup[0:3])#prints the first three elements of tuple
print(tup[-1])#prints the last element of tuple
print(len(tup))#prints the length of tuple
#if i want add remove or change a tuple item i must first convert the tuple into a list
countries=("Nepal","India","China")
temp=list(countries)#converts tuple into list
temp.append("Bhutan")#adds Bhutan to the list
temp.remove("China")#removes China from the list
countries=tuple(temp)#converts the list back into tuple
print(countries)#prints the new tuple