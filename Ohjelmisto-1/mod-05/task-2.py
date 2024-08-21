#kysytään lukuja kunnes tyhjä syöte for loopissa

def main():
    luvut = []
    for i in iter(int, 1):
        luku = input(f"Anna luku: ")
        if luku == "":
            break
        luvut.append(luku)
    print(f"5 suurinta lukua: {sorted(luvut, reverse=True)[:5]}")

if __name__ == "__main__":
    main()
