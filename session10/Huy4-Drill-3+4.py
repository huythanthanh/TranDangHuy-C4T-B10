#Drill 3 với drill 4 cộng lại làm 1 nhé anh...
huy = {
    'raichu' : 'has a regional variant that is Electric/Psychic. It evolves from Pikachu when exposed to a Thunder Stone. All Pikachu in Alola will evolve into this form regardless of their origin.',
    'onix' : 'resembles a giant chain of gray boulders that become smaller towards the tail. It has a rocky spine on its head and a pair of black eyes right beneath it. This Pokémon has a magnet in its brain that serves as an internal compass. Its body absorbs many hard objects, making its body very solid. As it grows older, it becomes more rounded and smoother, eventually becoming similar to black diamonds.'
}
while True:
    keyInput = input("Nhap tu khoa muon tim: ").lower()
    print (keyInput)
    if keyInput not in huy:
        print("Tu khoa khong co.")

    for key, value in huy.items():
        if keyInput == key:
            print(key, value)