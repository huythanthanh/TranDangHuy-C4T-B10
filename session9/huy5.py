import random
so1 = random.randint(-99,99)
so2 = random.randint(-99,99)
so3 = random.randint(-99,99)
so4 = random.randint(-99,99)
so5 = random.randint(-99,99)
print ("Dãy số: ", so1,so2,so3,so4,so5)
nhap = [so1,so2,so3,so4,so5]
chonso = int(input("Chọn 1 số bất kỳ:"))
if chonso == so1 or chonso == so2 or chonso == so3 or chonso == so4 or chonso == so5:
    print ("vị trí của ",chonso,"là:", nhap.index(chonso))

else:
    print ("Số này không có trong dãy")

