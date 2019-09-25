import random
huy = input("Nhap 1 thu: ")
shuffled = list(huy)
random.shuffle(shuffled)

for i in shuffled:
    print (i.upper())