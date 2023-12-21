import random
import requests

def get_random_cat_image(api_key):
    base_url = "https://api.thecatapi.com/v1/images/search"
    headers = {"x-api-key": api_key}

    try:
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()
        cat_data = response.json()

        if cat_data:
            cat_image_url = cat_data[0]["url"]
            return cat_image_url

        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching cat image: {e}")
        return None
    
    
def get_random_chuck_norris_joke():
    chuck_norris_joke_api_url = 'https://api.chucknorris.io/jokes/random'
    try:
        response = requests.get(chuck_norris_joke_api_url)
        response.raise_for_status()
        joke_data = response.json()

        return joke_data.get('value', "Failed to fetch Chuck Norris joke.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Chuck Norris joke: {e}")
        return "Failed to fetch Chuck Norris joke."


def get_random_advice():
    advice_api_url = "https://api.adviceslip.com/advice"
    try:
        response = requests.get(advice_api_url)
        response.raise_for_status()
        advice_data = response.json()

        return advice_data['slip']['advice']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching advice: {e}")
        return "Failed to fetch advice."


def get_random_fox_image():
    try:
        response = requests.get("https://randomfox.ca/floof/")
        response.raise_for_status()
        fox_data = response.json()

        fox_image_url = fox_data["image"]

        return fox_image_url

    except requests.exceptions.RequestException as e:
        print(f"Error fetching fox image: {e}")
        return "Failed to fetch a fox image."


def get_nasa_apod(api_key):
    base_url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": api_key,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        apod_data = response.json()
        title = apod_data.get("title", "Astronomy Picture of the Day")
        image_url = apod_data.get("url", "")
        explanation = apod_data.get("explanation", "No description available.")

        return {
            "title": title,
            "image_url": image_url,
            "explanation": explanation,
        }

    except requests.exceptions.RequestException as e:
        print(f"Error fetching NASA APOD: {e}")
        return None
    
def get_cat_fact():
    base_url = "https://catfact.ninja/fact"

    try:
        response = requests.get(base_url)
        response.raise_for_status()
        cat_fact_data = response.json()

        if cat_fact_data.get("fact"):
            return cat_fact_data["fact"]
        else:
            return "Unable to fetch cat fact."

    except requests.exceptions.RequestException as e:
        print(f"Error fetching cat fact: {e}")
        return "Unable to fetch cat fact."
