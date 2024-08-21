from urllib.parse import uses_relative


def gallons_to_liters(gallons):
    liters = gallons * 3.7854
    print(f"{gallons} gallonaa on {liters} litraa")



def main():
    while True:
        # Ask user for input
        gallons = float(input("Anna gallonat: "))

        #Check if input is negative

        if gallons < 0:
            break

        # Call function
        gallons_to_liters(gallons)

if __name__ == "__main__":
    main()
