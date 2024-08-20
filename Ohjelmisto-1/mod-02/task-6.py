import random

numerolukko_yksi = 0
numerolukko_kaksi = 0

# arvotaan 3 numeroinen koodi lukko ykköselle
for i in range(3):
    numerolukko_yksi = numerolukko_yksi * 10 + random.randint(0, 9)

# arvotaan 4 numeroinen koodi lukko kakkoselle
for i in range(4):
    numerolukko_kaksi = numerolukko_kaksi * 10 + random.randint(1, 6)

print("Lukko ykkösen koodi on", numerolukko_yksi)
print("Lukko kakkosen koodi on", numerolukko_kaksi)

