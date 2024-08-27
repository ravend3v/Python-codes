import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('WEATHER_API_KEY')

kaupunki = input("Anna kaupunki: ")


def hae_saa(paikkakunta):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={API_KEY}&units=metric'
    vastaus = requests.get(url)

    if vastaus.status_code != 200:
        return f"Error: Unable to fetch weather data for {paikkakunta}. Status code: {vastaus.status_code}"

    data = vastaus.json()

    if 'weather' not in data or 'main' not in data:
        return f"Error: Incomplete weather data received for {paikkakunta}."

    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']

    return {
        f"Sää paikkakunnalla {paikkakunta} on {weather_description}",
        f"Lämpötila paikkakunnalla {paikkakunta} on {temperature} °C"
    }


def main():
    saa = hae_saa(kaupunki)
    print(saa)


if __name__ == "__main__":
    main()

