import mysql.connector as mysql_connector
import geopy as gp
from geopy.distance import distance
import math


yhteys = mysql_connector.connect(
    host="localhost",
    port="3306",
    user="raven",
    password="password123",
    database="flight_game",
)

def hae_icao_koodit(icao):
    sql = "SELECT * FROM airport WHERE ident = %s"
    cursor = yhteys.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    tulokset = cursor.fetchall()
    cursor.close()
    return tulokset

syote1 = input("Anna ensimmäinen ICAO-koodi: ")
syote2 = input("Anna toinen ICAO-koodi: ")

def laske_kenttien_etaisyys():
    kentta1 = hae_icao_koodit(syote1)
    kentta2 = hae_icao_koodit(syote2)
    if len(kentta1) == 0 or len(kentta2) == 0:
        return "Kenttiä ei löytynyt"
    kentta1 = kentta1[0]
    kentta2 = kentta2[0]
    p1 = gp.Point(kentta1["latitude_deg"], kentta1["longitude_deg"])
    p2 = gp.Point(kentta2["latitude_deg"], kentta2["longitude_deg"])
    return round(distance(p1, p2).km)

print("Syöttämäsi lentokenttien etäisyys toisistaan on: ",laske_kenttien_etaisyys(), "km")
yhteys.close()






