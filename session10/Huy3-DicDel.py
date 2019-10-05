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