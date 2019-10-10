import random
skills = [
    {
        'Name':'Tackle',
        'Minimum level':1,
        'Damage':5,
        'Hit rate' : 0.3
    },
    {
        'Name':'Quick Attack',
        'Minimum level':2,
        'Damage':3,
        'Hit rate' : 0.5
    },
    {
        'Name':'Strong Kick',
        'Minimum level':4,
        'Damage':9,
        'Hit rate' : 0.2
    }
]

huy = int(input("Lever của nhân vật: "))
print("Chọn skill")

count = 0 

for skill in skills :
    count += 1
    print(count,". ",end = "")
    for key in skill:
        print(key, ': ', skill[key])
    print("\n")

chonskill = int(input("Chọn skill: "))

if(skills[chonskill - 1]['Minimum level'] > huy): print("Không thể dùng chiêu này :>")
else :    
    hit = random.uniform(0,1)
    
    if(hit > skills[chonskill - 1]['Hit rate']): print(skills[chonskill - 1]['Damage'])
    else: print("Trượt")

# Em cần anh bổ túc gấp về dòng 35 đến hết :) đồ trên mạng khó hiểu quá