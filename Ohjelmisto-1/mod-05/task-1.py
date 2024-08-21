arpakuutioiden_lukumäärä = int(input("Kuinka monta arpakuutiota heitetään? "))
heitot = []
arpakuuti = [1, 2, 3, 4, 5, 6]

#heitetään arpakuutioita automaattisesti ja lisätään heitot-listaan
for i in range(arpakuutioiden_lukumäärä):
    import random
    heitto = random.choice(arpakuuti)
    heitot.append(heitto)

heitot.sort()
print("Heittojen summa: ", sum(heitot))
