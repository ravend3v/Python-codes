import requests

def api_request(url):
    response = requests.get(url)
    return response.json()

def main():
    url = "https://api.chucknorris.io/jokes/random"
    data = api_request(url)
    print(data["value"])

if __name__ == "__main__":
    main()
    