import random
def random_number():
    return random.randint(1, 6)

# Pää funktio joka kutsii random_number funktiota kunnes silmäluku on 6
def main():
    while True:
        number = random_number()
        print(number)
        if number == 6:
            break