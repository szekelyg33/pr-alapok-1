#feladat_001
"""
kérjük be a billentyűzetről a nevünket, és irassuk ki a képernyőre! a billentyűzetről mindig szöveget(stringet)olvasunk be!
type(változó)
"""
'''
nev = input ("kerek egy nevet: ")
print(f"a megadott nev kovetkezo: {nev}")
'''
vnev  = input("kerek egy vezeteknevet: ")
knev = input("kerek egy keresztnevet ")

print(f"a megadott nev a kovetkezo: {knev} {vnev}")
print(f"a vnev valtozo tipusa: {type(knev)}")
print(f"a knev valtozo tipusa:{type(vnev)}")