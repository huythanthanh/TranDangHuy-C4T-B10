nhapso = int(input("Nhap 1 thang trong nam:"))
if nhapso <= 7 and nhapso % 2 == 1:
    print ("Thang", nhapso, "co 31 ngay")

elif nhapso >= 8 and nhapso % 2 == 0:
    print ("Thang", nhapso, "co 31 ngay")

elif nhapso <= 7 and nhapso % 2 == 0:
    print ("Thang", nhapso, "co 30 ngay")

elif nhapso >= 7 and nhapso % 2 == 1:
    print ("Thang", nhapso, "co 30 ngay")
        
else:
    print ("Thang 2 co 28-29 ngay :))")