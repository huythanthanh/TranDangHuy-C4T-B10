import random
shuffled = list(huy)
random.shuffle(shuffled)
print (shuffled, sep = "")
nhap = input ("Nhap chu: ")
if nhap == shuffled:
    print("Nhap dung")
else:
    print("Nhap sai")