listword = ['ST','BĐ','BTL','CG','DD','HBT']
count = 0
print ("Danh sách tên các quận:")
#Lập danh sách các quận kèm theo thứ tự
for i in listword:
    count += 1
    print (count,".",i.upper())

dem = 0
huy = ['150,300','247,100','333,300','266,800','420,900','318,000']
#Cái này là em lập danh sách để tìm max nhé =)))
huy1 = [150300,247100,333300,266800,420900,318000]

print ("Danh sách dân số từng quận theo thứ tự:")  
for i in huy:
    dem += 1
    print (dem, '.', i)  
#Tìm dân số max min
print ("Dân số cao nhất trong các quận là:", max(huy1))
print ("Dân số thấp nhất trong các quận là:", min(huy1))
if max(huy1) == 420900:
    print ("Quận có dân số cao nhất là DD, rộng 9,96 km2")
elif min(huy1) == 150300:
    print ("Quận có dân số thấp nhất là ST, rộng 117,3 km2")
# Đề ko cho input output em khó tưởng tượng đc cách làm :((
# Em lười nên tích hợp cả part 5 vào 1 cái nhé anh :>
