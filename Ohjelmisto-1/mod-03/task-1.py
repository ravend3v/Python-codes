kuha_pituus = int(input("Kuinka pitkä kuha oli? "))

if kuha_pituus <= 37:
    print("Kuha on alamittainen, laske kuha takaisin järveen.")
    print(f"Kuha oli {37-kuha_pituus} senttiä liian lyhyt.")

else:
    print("Kuha on sallittu")

