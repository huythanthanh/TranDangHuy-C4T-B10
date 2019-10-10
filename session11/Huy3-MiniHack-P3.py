maytinh = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30
}
toshiba = {
    'TOSHIBA' : 10
}
fujitsu = {
    'FUSJITSU' : 15
}
alienware = {
    'ALIENWARE' : 5
}
maytinh.update(toshiba)
maytinh.update(fujitsu)
maytinh.update(alienware)

for key, value in maytinh.items():
    print (key,':', value)

tong = sum(maytinh.values())
print ("Tong so luong may tinh: ", tong)