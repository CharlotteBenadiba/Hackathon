import requests

API_KEY = '4eb1b83459cbe02d93974fbe71bae0ac'
BASE_URL = 'https://api.themoviedb.org/3'

def fetch_movie_data(movie_name):
    url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={movie_name}"
    response = requests.get(url)
    return response.json()

def fetch_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}"
    response = requests.get(url)
    return response.json()
