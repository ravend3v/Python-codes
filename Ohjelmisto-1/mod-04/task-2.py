while True:
    tuumat = int(input("Anna pituus tuumina: "))

    if tuumat < 0:
        break
    else:
        cm = tuumat * 2.54
        print(f"{tuumat} tuumaa on {cm:.2f} senttimetriä.")

