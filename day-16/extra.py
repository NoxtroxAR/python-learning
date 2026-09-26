import random
#for loop with else statement
#when for loop is finshed the else will get executed
for i in range(5):
    print(i)
else:
    print("Hello")
#else can be used like this with while loop as well
a=random.randint(1,3)#gives random num between 1-3 
print(a)
#random floating point number
a=random.random()
print(a)
#lests use a tuple
a=("rock","Paper","Scissor")
choice=random.choice(a)
print(f"The computer chose {choice}")
#lets use a list now
cards=["2",'3','4','5']
random.shuffle(cards)
print(cards)