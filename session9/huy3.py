listword = ['blue','red','green']
mau = input("Thêm màu:")
listword.append(mau)
count = 0
xoa1 = input("Nhập màu muốn xóa:")
listword.remove(xoa1)
print("Danh sách màu mới:")
for i in listword:
    count += 1
    
    print (count,".",i.upper())

vitri = int(input("nhap vi tri muon xoa: "))
listword.pop(vitri)

print ("Danh sách màu mới:")
for i in listword:
    count += 1
    
    print (count,".",i.upper())