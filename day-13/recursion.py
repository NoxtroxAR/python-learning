#factorial using recurion
def fact(n):
    if n==0:
        return 1
    else:
        return (n*(fact(n-1)))
print(fact(5))
#Sum of number using recursion
def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
print(sum(5))