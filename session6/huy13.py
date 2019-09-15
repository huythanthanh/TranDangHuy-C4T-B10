while True:
    email = input("nhap email:")
    taikhoan = input ("Nhap tai khoan:")
    matkhau = input ("nhap mat khau:")
    matkhau2 = input ("nhap lai mat khau:")
    if '@gmail.com' in email:
        print ("nhap tai khoan thanh công")
        break
    else:
        print ("nhap tai khoan khong thanh cong, vui long nhap lai") 

        