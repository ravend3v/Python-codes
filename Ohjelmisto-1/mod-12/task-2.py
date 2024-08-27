import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('WEATHER_API_KEY')

kaupunki = input("Anna kaupunki: ")

# Get the api key from the env file
def hae_saa(paikkakunta):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={API_KEY}&units=metric'
    vastaus = requests.get(url)

    # Translate the data to Finnish
    data = {
        f"Sää paikkakunnalla {paikkakunta} on {vastaus.json()['weather'][0]['description']}",
        f"Lämpötila paikkakunnalla {paikkakunta} on {vastaus.json()['main']['temp']} °C"
    }
    return data

def main():
    saa = hae_saa(kaupunki)
    print(saa)

if __name__ == "__main__":
    main()

