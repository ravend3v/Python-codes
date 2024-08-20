biologinen_sukupuoli = str(input("Anna biologinen sukupuoli (mies/nainen): "))
hemoglobiiniarvo = int(input("Anna hemoglobiiniarvo: "))

if biologinen_sukupuoli == "mies":
    if hemoglobiiniarvo > 134 & hemoglobiiniarvo < 195:
        print("Hemoglobiiniarvo on normaali.")

    elif hemoglobiiniarvo < 134:
        print("Hemoglobiiniarvo on alhainen.")

    elif hemoglobiiniarvo > 195:
        print("Hemoglobiiniarvo on korkea.")

elif biologinen_sukupuoli == "nainen":
    if hemoglobiiniarvo > 117 & hemoglobiiniarvo < 175:
        print("Hemoglobiiniarvo on normaali.")

    elif hemoglobiiniarvo < 117:
        print("Hemoglobiiniarvo on alhainen.")

    elif hemoglobiiniarvo > 175:
        print("Hemoglobiiniarvo on korkea.")