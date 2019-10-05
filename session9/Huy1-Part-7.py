listword = [45,67,56,78]

count = 0
listword.sort(reverse=True)
print ("High scores:")
for i in listword:
    count += 1
    print (count,".", i)

while True:
    nhap = int(input("Ente, your your new high score:"))
    danhsach = [45,67,56,78,nhap]
    danhsach.sort(reverse=True)
    dem = 0
    print ("High scores:")
    for i in range(5):
        dem += 1
        print (dem,".", danhsach[i])    