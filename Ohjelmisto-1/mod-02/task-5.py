leiviskat = input("Anna leiviskät: ")
naulat = input("Anna naulat: ")
luodit = float(input("Anna luodit: "))

yht_kilogrammat = (int(leiviskat) * 20 * 32 * 13.3 + int(naulat) * 32 * 13.3 + luodit * 13.3) / 1000
yht_grammat = (int(leiviskat) * 20 * 32 * 13.3 + int(naulat) * 32 * 13.3 + luodit * 13.3) % 1000

print("Massa nykymittojen mukaan: ")
print (f"{yht_kilogrammat:.2f} kilogrammaa ja {yht_grammat:.2f} grammaa")