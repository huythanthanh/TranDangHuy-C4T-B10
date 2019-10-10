#Bài này với bài drill 1 em làm ở đây nhé... hình như drill 1 em làm sai ý .-. anh check hộ e
huy = {
    'Name' : 'Nezuko',
    'Age' : 16,
    'Descripton' : 'she is a girl'
}
print (huy)
huy ['Super power'] = 'Monster'
nhap = input("Them mo ta: ")
i = input("Noi dung phan mo ta: ")
huy [nhap] = i
print (huy)

xoa = input("Nhap phan muon xoa:")
del huy[xoa]
print (huy)    

if 'Name' in huy:
    print ("Key 'name' exist in my dictionary")
elif 'Name' not in huy:
    print ("Key 'name' does not exist in my dictionary")
elif 'Nationality' in huy:
    print ("Key 'Nationality' exist in my dictionary")
else:
    print ("Key 'Nationality' does not exist in my dictionary")