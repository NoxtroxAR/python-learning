#Set methods are
a={1,2,3}
b={3,4,5}
c={6,7}
d={1,2}
print(a.union(b))
print(a.intersection(b))
#a.update(b)#Updates the set a itself rather then creating the new set
#print(a)#{1, 2, 3, 4, 5}
print(a.symmetric_difference(b))
print(a.difference(b))
print(a.isdisjoint(b))#false
print(a.isdisjoint(c))#true
print(d.issubset(a))#true
a.add(4)
print(a)
a.remove(3)
print(a)
item=a.pop()#random value gets pooped
print(a)
print(item)
del a#deletes the entire set
b.clear()
print(b)
'''
1) union()---->creates a new set with the unique elements from both the sets
2)update()----->applied on a set itself and it also adds unique elements from the both the sets into one of the sets
3) intersection()----> creates a new set with the common elements from both the sets
4)intersection_update()------> applied on a set itself and it also contains the common elements from both the sets
5)symmetric_difference--------> creates a new set with the elements from the both the sets that are not common in between
6)symmetric_difference_update-------> applied on a set itself and it contains elements from the sets that are not common inj between
7)difference------> creates a new set with the elements from a single set that are not common 
8) difference_update-----> applied on a set itself and contains elements of a set that are not common

9)isdisjoint()---->checks if there are common elements between two sets
10)issuperset----> checks if a set is a superset of another set
11) issubset-----> checks is a set is subset of another set
12)add------> to add a element into a set
13) remove-------> to remove an elements from a set, but raises key error if the element is not present in the set
14) discard-----> to remove an element from a set, does not raises error if the lement is not present in the set
15) del------> not method, a keyword, to delete the complete set
16) clear-------> to clear all the elements of a set 
17) in keyword used to check if a element is present in the set or not
18) pop()-----> to remove a random element from the set and also we can get that element
'''