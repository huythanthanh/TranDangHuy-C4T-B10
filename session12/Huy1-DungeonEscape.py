import random
print ("Level 1 !!!")
player = {
    "x": 2,
    "y": 2
}

escape = {
    "x": 2,
    "y": 3
}

key = {
    "x": 4,
    "y": 4
}

flag = False

while True:
    for i in range(4):
        for j in range(4):
            if (i == player['y'] - 1) and (j == player['x'] - 1):
                print("P", end=" ")
            elif (i == escape['y'] - 1) and (j == escape['x'] - 1):
                print("E", end=" ")
            elif (i == key['y'] - 1) and (j == key['x'] - 1):
                if flag == False:
                    print("K", end=" ")
                else:
                    print("-", end=" ")
            else:
                print("-", end=" ")
        print()

    move = input("Your move ? ")

    

    if move == "w":
        player['y'] -= 1
        if player["y"] == 0:
            print("Out of move !!!!") 
            player['y'] += 1 
    if move == "s":
        player['y'] += 1
        if player["y"] > 4:
            print("Out of move !!!!") 
            player['y'] -= 1
    if move == "a":
        player['x'] -= 1
        if player["x"] == 0:
            print("Out of move !!!!") 
            player['x'] += 1 
    if move == "d":
        player['x'] += 1
        if player["x"] > 4:
            print("Out of move !!!!") 
            player['x'] -= 1 

    if (player['x'] == key['x']) and (player['y'] == key['y']):
        print("Found key !!!!")
        flag = True
    
    if (player['x'] == escape['x']) and (player['y'] == escape['y']): 
        if flag == False:
            print("Need key !!!")
        else:
            print("You won !!!!")
            for i in range(4):
                for j in range(4):
                    if (i == player['y'] - 1) and (j == player['x'] - 1):
                        print("P", end=" ")
                    elif (i == escape['y'] - 1) and (j == escape['x'] - 1):
                        print("E", end=" ")
                    elif (i == key['y'] - 1) and (j == key['x'] - 1):
                        if flag == False:
                            print("K", end=" ")
                        else:
                            print("-", end=" ")
                    else:
                        print("-", end=" ")
                print()
            
            break
            

print ("Level 2 !!!")
player = {
    "x": 2,
    "y": 2
}

escape = {
    "x": 2,
    "y": 3
}

key1 = {
    "x": 4,
    "y": 4
}

key2 = {
    "x": 5,
    "y": 6
}
flag = False
flag2 = False

while True:
    for i in range(6):
        for j in range(6):
            if (i == player['y'] - 1) and (j == player['x'] - 1):
                print("P", end=" ")
            elif (i == escape['y'] - 1) and (j == escape['x'] - 1):
                print("E", end=" ")
            elif (i == key['y'] - 1) and (j == key['x'] - 1):
                if flag == False:
                    print("K", end=" ")
                else:
                    print("-", end=" ")
            
            elif (i == key2['y'] - 1) and (j == key2['x'] - 1):
                if flag2 == False:
                    print("K", end=" ")
                else:
                    print("-", end=" ")
            else:
                print("-", end=" ")
        print()

    move = input("Your move ? ")

    

    if move == "w":
        player['y'] -= 1
        if player["y"] == 0:
            print("Out of move !!!!") 
            player['y'] += 1 
    if move == "s":
        player['y'] += 1
        if player["y"] > 6:
            print("Out of move !!!!") 
            player['y'] -= 1
    if move == "a":
        player['x'] -= 1
        if player["x"] == 0:
            print("Out of move !!!!") 
            player['x'] += 1 
    if move == "d":
        player['x'] += 1
        if player["x"] > 6:
            print("Out of move !!!!") 
            player['x'] -= 1 

    if (player['x'] == key['x']) and (player['y'] == key['y']):
        print("Found 1 key !!!!")
        flag = True
    if (player['x'] == key2['x']) and (player['y'] == key2['y']):
        print("Found 1 key !!!!")
        flag2 = True
    
    if (player['x'] == escape['x']) and (player['y'] == escape['y']): 
        if flag == False or flag2 == False:
            print("Need key !!!")
        else:
            print("You won !!!!")
            for i in range(4):
                for j in range(4):
                    if (i == player['y'] - 1) and (j == player['x'] - 1):
                        print("P", end=" ")
                    elif (i == escape['y'] - 1) and (j == escape['x'] - 1):
                        print("E", end=" ")
                    elif (i == key['y'] - 1) and (j == key['x'] - 1):
                        if flag == False:
                            print("K", end=" ")
                        else:
                            print("-", end=" ")
                    else:
                        print("-", end=" ")
                print()
            
            break
            

print ("Level 3 !!!")
player = {
    "x": 2,
    "y": 2
}

escape = {
    "x": 2,
    "y": 3
}

key1 = {
    "x": 4,
    "y": 4
}

key2 = {
    "x": 6,
    "y": 7
}

monster = {
    "x": random.uniform(1,7),
    "y": random.uniform(1,7)
}

monster2 = {
    "x": random.uniform(1,7),
    "y": random.uniform(1,7)
}
flag = False
flag2 = False
flag3 = False
flag4 = False

while True:
    for i in range(8):
        for j in range(8):
            if (i == player['y'] - 1) and (j == player['x'] - 1):
                print("P", end=" ")
            elif (i == monster['y'] - 1) and (j == monster['x'] - 1):
                print("M", end=' ')
            elif (i == monster2['y'] - 1) and (j == monster2['x'] - 1):
                print("M", end=' ')
            elif (i == escape['y'] - 1) and (j == escape['x'] - 1):
                print("E", end=" ")
            elif (i == monster['y'] - 1) and (j == monster['x'] - 1):
                if flag3 == False:
                    print("M", end=" ")
                else:
                    print("-", end=" ")
            elif (i == monster2['y'] - 1) and (j == monster2['x'] - 1):
                if flag4 == False:
                    print("M", end=" ")
                else:
                    print("-", end=" ")
            elif (i == key['y'] - 1) and (j == key['x'] - 1):
                if flag == False:
                    print("K", end=" ")
                else:
                    print("-", end=" ")
            
            elif (i == key2['y'] - 1) and (j == key2['x'] - 1):
                if flag2 == False:
                    print("K", end=" ")
                else:
                    print("-", end=" ")
            else:
                print("-", end=" ")
        print()

    move = input("Your move ? ")

    if move == "w":
        player['y'] -= 1
        if player["y"] == 0:
            print("Out of move !!!!") 
            player['y'] += 1 
    if move == "s":
        player['y'] += 1
        if player["y"] > 8:
            print("Out of move !!!!") 
            player['y'] -= 1
    if move == "a":
        player['x'] -= 1
        if player["x"] == 0:
            print("Out of move !!!!") 
            player['x'] += 1 
    if move == "d":
        player['x'] += 1
        if player["x"] > 8:
            print("Out of move !!!!") 
            player['x'] -= 1 

    if (player['x'] == monster['x']) and (player['y'] == monster['y']):
        decision = input("Fight, Run away or Defend")
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
        flag = True

    

    if (player['x'] == key['x']) and (player['y'] == key['y']):
        print("Found 1 key !!!!")
        flag = True
    if (player['x'] == key2['x']) and (player['y'] == key2['y']):
        print("Found 1 key !!!!")
        flag2 = True
    
    if (player['x'] == escape['x']) and (player['y'] == escape['y']): 
        if flag == False or flag2 == False:
            print("Need key !!!")
        else:
            print("You won !!!!")
            for i in range(4):
                for j in range(4):
                    if (i == player['y'] - 1) and (j == player['x'] - 1):
                        print("P", end=" ")
                    elif (i == escape['y'] - 1) and (j == escape['x'] - 1):
                        print("E", end=" ")
                    elif (i == key['y'] - 1) and (j == key['x'] - 1):
                        if flag == False:
                            print("K", end=" ")
                        else:
                            print("-", end=" ")
                    else:
                        print("-", end=" ")
                print()
            
            break