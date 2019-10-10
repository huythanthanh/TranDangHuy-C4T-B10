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

print ('ASUS : ', giatien['ASUS'])
nhap = input("Nhap ten may: ").upper()
print (nhap,':', giatien[nhap])