listword = ['ST','BĐ','BTL','CG','DD','HBT']
count = 0
print ("Danh sách tên các quận:")
#Lập danh sách các quận kèm theo thứ tự
for i in listword:
    count += 1
    print (count,".",i.upper())

dem = 0
huy = [150300,247100,333300,266800,420900,318000]
print ("Danh sách dân số từng quận theo thứ tự:")  
for i in huy:
    dem += 1
    print (dem, '.', i)  
#Tìm dân số max min
print ("Dân số cao nhất trong các quận là:", max(huy))
if max(huy) == 420900:
    print ("Quận có dân số cao nhất là DD")