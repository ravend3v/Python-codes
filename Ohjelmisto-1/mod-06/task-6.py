def pizza_hinta(halkaisija, hinta):
    pinta_ala = 3.14159 * (halkaisija / 2) ** 2
    yksikkohinta = hinta / pinta_ala
    return yksikkohinta

def main():
    halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija: "))
    hinta1 = float(input("Anna ensimmäisen pizzan hinta: "))
    yksikkohinta1 = pizza_hinta(halkaisija1, hinta1)

    halkaisija2 = float(input("Anna toisen pizzan halkaisija: "))
    hinta2 = float(input("Anna toisen pizzan hinta: "))
    yksikkohinta2 = pizza_hinta(halkaisija2, hinta2)

    if yksikkohinta1 < yksikkohinta2:
        print(f"Ensimmäinen pizza on parempi ({yksikkohinta1:.2f} €/cm^2 < {yksikkohinta2:.2f} €/cm^2)")
    else:
        print(f"Toinen pizza on parempi ({yksikkohinta2:.2f} €/cm^2 < {yksikkohinta1:.2f} €/cm^2)")

main()

