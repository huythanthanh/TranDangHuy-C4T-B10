nhapso = int(input("Nhap 1 so bat ky > 0:"))
r1 = range (nhapso ,0,-2)
r2 = range (nhapso - 1, 0, -2)
if nhapso % 2 == 1:
    print (*r1)

else:
    print (*r2) 