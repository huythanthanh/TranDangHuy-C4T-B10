listword = [117.43,9.224,43.35,12.04,9.96,10.09]

count = 0
print ("Dien tich cua cac quan:")
for i in listword:
    count += 1
    print (count,".", i)
ST = 150300 // 117.43
BD = 247100//9.224
BTL = 333300 // 43.35
CG = 266800 // 12.04
DD = 420900 // 9.96
HBT = 31800 // 10.09
dem = 0
huy = [ST,BD,BTL,CG,DD,HBT]
print ("Mat do dan so (nguoi/km2):")  
for i in huy:
    dem += 1
    print (dem, '.', i)  

tong = ST + BD + BTL + CG + DD + HBT
print ("Mat do dan cu trung binh (nguoi/km2):", tong//6)    