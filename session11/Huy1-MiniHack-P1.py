maytinh = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30
}
print(maytinh)
print ('MACBOOK:', maytinh['MACBOOK'])
nhap = input("Nhap hang may tinh: ").upper()
print (nhap,':', maytinh[nhap])
toshiba = {
    'TOSHIBA' : 10
}
maytinh.update(toshiba)
print(maytinh)