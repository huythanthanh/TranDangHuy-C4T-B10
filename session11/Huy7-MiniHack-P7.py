TextAdventure = {
    'Name' : 'Light',
    'Age' : 17,
    'Streght' : 8,
    'Defense' : 10,
    'HP' : 100,
    'Backpack' : 'Shield, Bread loaf',
    'Gold' : 100,
    'Level' : 2,

}
TextAdventure['Gold'] = 150
TextAdventure['Backpack'] = 'Shield, Bread loaf, Flint Stone'
pocket = {
    'Pocket' : 'MonsterDex, Flashlight'
}

TextAdventure.update(pocket)
print(TextAdventure)        