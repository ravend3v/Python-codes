import mysql.connector as mysql_connector


yhteys = mysql_connector.connect(
    host="localhost",
    user="raven",
    password="password123",
    database="flight_game",
)

def get_country_code(iso_country):
    cursor = yhteys.cursor()
    cursor.execute("SELECT type FROM airport WHERE iso_country = %s", (iso_country,))

    #sortataan tulokset typen mukaan ja kertoo niiden määrät
    results = cursor.fetchall()
    type_counts = {}
    for result in results:
        if result[0] in type_counts:
            type_counts[result[0]] += 1
        else:
            type_counts[result[0]] = 1

    return type_counts

# Kysytään käyttäjältä maakoodi ja tulostetaan sen lentokenttien tyypit
usr_input = str(input("Anna maakoodi (esim. FI): "))
print(get_country_code(usr_input))

yhteys.close()

