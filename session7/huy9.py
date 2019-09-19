giatri = input("Nhap phan tu muon xoa: ")
nhap = ['sport','LOL','BTS']
if giatri in nhap:
    nhap.remove(giatri)
    print (*nhap, sep=',')
else:
    print ("Khong co",giatri," ...")