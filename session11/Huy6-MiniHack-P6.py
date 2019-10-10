soluong = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30
}
soluong['DELL'] = 70
soluong['MACBOOK'] = 10

toshiba = {
    'TOSHIBA' : 10
}
fujitsu = {
    'FUJITSU' : 15
}
alienware = {
    'ALIENWARE' : 5
}
soluong.update(toshiba)
soluong.update(fujitsu)
soluong.update(alienware)

giatien = {
    'HP' : 600,
    'DELL' : 650,
    'MACBOOK' : 12000,
    'ASUS' : 400,
    'ACER' : 350,
    'TOSHIBA' : 600,
    'FUJITSU' : 900,
    'ALIENWARE' : 1000
}
count = 0
for key in soluong:
    tong = giatien[key] *soluong[key]
    count += tong

print ('Tong: ', count)