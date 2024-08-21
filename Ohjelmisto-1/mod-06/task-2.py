import random
def user_input():
    maksimi_luku = int(input("Mikä on nopan maksimi silmäluku? "))

    return maksimi_luku
def main():
    maksimi_luku = user_input()

    while True:
        number = random.randint(1, maksimi_luku)
        print(number)
        if number == maksimi_luku:
            break

main()
