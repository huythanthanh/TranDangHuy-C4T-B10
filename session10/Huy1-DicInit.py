#Init + Input làm chung 1 bài anh nhé
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
keyInput = input("Nhap key muon tim: ")

if keyInput not in huy:
    print("Key not exist")

for key, value in huy.items():
    if keyInput == key:
        print(key, "-", value)
    
    