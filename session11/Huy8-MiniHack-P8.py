skill1 = ['Name: Tackle','Minimum level: 1','Damage: 5','Hit rate: 0.3']
skill2 = ['Name: Quick attack','Minimum level: 2','Damage: 3','Hit rate: 0.5']
skill3 = ['Name: Strong Kick','Minimum level: 4','Damage: 9','Hit rate: 0.2']
count = 0
print ("Skill 1:") 
for i in skill1:
    count += 1
    print (count,'.', i)

chieu_hai = 0
print (" ")
print ("Skill 2:")
for i in skill2:
    chieu_hai += 1
    print (chieu_hai, '.', i)

chieu_ba = 0
print (" ")
print ("Skill 3:")
for i in skill3:
    chieu_ba += 1
    print(chieu_ba,'.',i)

