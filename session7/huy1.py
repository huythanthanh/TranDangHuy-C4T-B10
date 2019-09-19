import random
so1 = random.randint(1,30)
so2 = random.randint(1,30)
saiso = random.randint (-3,3)
sum = so1 + so2 + saiso
print ("{} + {}  = {}". format(so1,so2,sum))
traloi = input("True or False: ").lower()
if traloi == "t" :
    if saiso == 0:
        print ("correct")
    else:
        print ("wrong")

elif traloi == "f":
    if saiso == 0:
        print ("wrong")
    else:
        print ("correct")