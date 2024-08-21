import random

def parilliset(lista = []):
    parilliset = []
    for i in lista:
        if i % 2 == 0:
            parilliset.append(i)
    return parilliset

def main():
    lista = []
    for i in range(10):
        lista.append(random.randint(1, 10))
    print(lista)
    print(parilliset(lista))

if __name__ == "__main__":
    main()