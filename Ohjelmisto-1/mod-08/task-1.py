import mysql.connector as mysql_connector

# Luodaan yhteys tietokantaan
yhteys = mysql_connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='raven',
    password='password123',
    autocommit=True
)

# Tarkistetaan onnistuiko yhteys
if yhteys.is_connected():
    print('Yhteys tietokantaan onnistui')
else:
    print('Yhteys tietokantaan epäonnistui')


def get_airport_name(icao):
    kursori = yhteys.cursor()

    kursori.execute('SELECT name FROM airport WHERE ident = %s', (icao,))

    tulos = kursori.fetchone()

    kursori.close()

    return tulos[0] if tulos else None

user_iput = input('Anna lentokentän ICAO-koodi: ')

if get_airport_name(user_iput):
    print(f'Lentokentän nimi on {get_airport_name(user_iput)}')
else:
    print('Lentokenttää ei löytynyt')

# Suljetaan yhteys
yhteys.close()








