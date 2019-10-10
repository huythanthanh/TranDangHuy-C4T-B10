giatien = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30
}
giatien['DELL'] = 70
giatien['MACBOOK'] = 10

toshiba = {
    'TOSHIBA' : 10
}
fujitsu = {
    'FUSJITSU' : 15
}
alienware = {
    'ALIENWARE' : 5
}
giatien.update(toshiba)
giatien.update(fujitsu)
giatien.update(alienware)

keyInput = input("Nhap ten: ").upper()
soluong = int(input("Nhap so luong: "))
for key, value in giatien.items():
    if keyInput == key:
        if value < soluong:
            print ("Khong du may !!")
        else:
            print('Ten may:',key,': So may con lai:', value - soluong)
