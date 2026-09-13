import time
currenthour=int(time.strftime('%H'))
#the above code will gather the curretn hour in a  sting from '00' to '24'
#we convert it into int
if(4<=currenthour<=12):
 print("Good morning")
elif(12<currenthour<=17):
 print("Good afternoon")
elif(17<currenthour<=20):
 print("Good evening")
else:
 print("Goodnight")