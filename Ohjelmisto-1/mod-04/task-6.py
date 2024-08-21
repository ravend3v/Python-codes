import random



def main():
    n = int(input("Arvottavien pisteiden määrä: "))
    n_inside = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 < 1:
            n_inside += 1
    pi = 4 * n_inside / n
    print("Piin likiarvo:", pi)

main()
