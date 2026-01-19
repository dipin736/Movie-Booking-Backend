import requests
from django.conf import settings

OMDB_BASE_URL = "https://www.omdbapi.com/"

def search_movies(title):
    params = {
        "apikey": settings.OMDB_API_KEY,
        "s": title
    }
    response = requests.get(OMDB_BASE_URL, params=params, timeout=5)
    response.raise_for_status()
    return response.json()

def get_movie_details(imdb_id):
    params = {
        "apikey": settings.OMDB_API_KEY,
        "i": imdb_id
    }
    response = requests.get(OMDB_BASE_URL, params=params, timeout=5)
    response.raise_for_status()
    return response.json()
