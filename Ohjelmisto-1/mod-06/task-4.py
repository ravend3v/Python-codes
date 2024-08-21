import random
def numero_summa(lista= []):
    summa = 0
    for i in lista:
        summa += i
    return summa

def main():
    lista = []
    for i in range(10):
        lista.append(random.randint(1, 10))
    print(lista)
    print(numero_summa(lista))

if __name__ == "__main__":
    main()