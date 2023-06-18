import requests

def fetch_pirate_jokes():
    response = requests.get("https://icanhazdadjoke.com/search?term=pirate", headers={"Accept": "application/json"})

    if response.status_code == 200:
        data = response.json()
        jokes = data["results"]
        
        for joke in jokes:
            print(joke["joke"])
    else:
        print("Failed to fetch pirate jokes.")


fetch_pirate_jokes()