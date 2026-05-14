import requests

def fetch_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            joke = response.json()
            print("Here is a random joke for you:")
            print(f"- {joke['setup']}")
            print(f"- {joke['punchline']}")
        else:
            print("Failed to fetch joke. Status code:", response.status_code)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_random_joke()
