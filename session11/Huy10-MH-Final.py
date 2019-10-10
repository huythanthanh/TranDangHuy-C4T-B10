skills = [
    {
        'Name':'Tackle',
        'Minimum level':1,
        'Damage':5,
        'Hit rate' : 0.3,
    },
    {
        'Name':'Quick Attack',
        'Minimum level':2,
        'Damage':3,
        'Hit rate' : 0.5,
    },
    {
        'Name':'Strong Kick',
        'Minimum level':4,
        'Damage':9,
        'Hit rate' : 0.2,
    }
]

huy = int(input("Nhập level nhân vật: "))
print("Chọn skill")

count = 0 

for skill in skills :
    count+=1
    print(count,". ",end = "")
    for key in skill:
        print(key, ': ',skill[key])
    print("\n")

chon_skill = int(input("Chọn skill: "))
if(skills[chon_skill-1]['Minimum level'] > huy): print("Không thể dùng chiêu này :>")
else :
    print(skills[chon_skill-1]['Minimum level'])

# Nó chỉ đơn giản là phép so sánh thôi đúng ko anh :)?? right :)???    