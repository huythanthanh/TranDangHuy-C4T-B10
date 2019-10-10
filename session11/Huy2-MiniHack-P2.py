maytinh = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30
}
toshiba = {
    'TOSHIBA' : 10
}
maytinh.update(toshiba)
print(maytinh)
nhap = input("Nhap ten may: ").upper()
soluong = int(input("Nhap so luong: "))
them = {
    nhap : soluong
}
maytinh.update(them)
print(maytinh)
maytinh['TOSHIBA'] = 20
maytinh['MACBOOK'] = 2
print(maytinh)