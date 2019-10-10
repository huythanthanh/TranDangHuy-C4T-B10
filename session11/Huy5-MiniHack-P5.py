giatien = {
    'HP' : 600,
    'DELL' : 650,
    'MACBOOK' : 12000,
    'ASUS' : 400,
    'ACER' : 350,
    'TOSHIBA' : 600,
    'FUJITSU' :900,
    'ALIENWARE' : 1000
}
print('Tong don hang:  -ASUS :', giatien['ASUS'] * 5)
ten = input("Nhap ten may: ").upper()
soluong = int(input("Nhap so luong ban duoc: "))
print('Tong don hang 2: ', ten,':', giatien[ten] * soluong)