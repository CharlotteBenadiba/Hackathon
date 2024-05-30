import requests
import random

API_KEY = '4eb1b83459cbe02d93974fbe71bae0ac'
BASE_URL = 'https://api.themoviedb.org/3'
genre_dict = {28: 'Action', 12: 'Adventure', 16: 'Animation', 35: 'Comedy', 80: 'Crime', 99: 'Documentary', 18: 'Drama',
              10751: 'Family', 14: 'Fantasy', 36: 'History', 27: 'Horror', 10402: 'Music', 9648: 'Mystery',
              10749: 'Romance', 878: 'Science Fiction', 10770: 'TV Movie', 53: 'Thriller', 10752: 'War', 37: 'Western'}


def fetch_movie_data(movie_name):
    url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={movie_name}"
    response = requests.get(url)
    return parse_info(response.json(), 'search')


def fetch_movie_by_genre(user_genre):
    genre_id = ''
    for code, genre in genre_dict.items():
        if genre.lower() == user_genre:
            genre_id = code
            break

    if genre_id:
        url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}"
        response = requests.get(url)
        return parse_info(response.json(), 'genre', user_genre)
    else:
        print("Invalid genre.")
        return None


def fetch_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}"
    response = requests.get(url)
    return parse_info(response.json())


def parse_info(raw_info, source, user_genre=None):
    if 'results' in raw_info:
        movies = []
        for info in raw_info['results']:
            genre_names = [genre_dict[genre] for genre in info.get('genre_ids', [])]
            genre_string = ', '.join(genre_names)
            if user_genre and user_genre.lower() not in genre_string.lower():
                continue  # Skip movies that don't match the requested genre
            movie_info = {
                'Title': info.get('title'),
                'Release_date': info.get('release_date'),
                'Overview': info.get('overview'),
                'Genres': genre_string,
                'Rating': info.get('vote_average'),
                'Number of ratings': info.get('vote_count')
            }
            movies.append(movie_info)

        if source == 'search':
            return movies[0] if movies else None
        elif source == 'genre' or source == 'recommendations':
            return movies
    else:
        return None

#  -------------------------new mariia
def fetch_movie_by_genre_and_year(genre, year):
    genre_id = ''
    for code, name in genre_dict.items():
        if name.lower() == genre.lower():
            genre_id = code
            break

    if genre_id:
        url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&primary_release_year={year}&with_genres={genre_id}"
        response = requests.get(url)
        return parse_info(response.json(), 'genre', genre)
    else:
        print("Invalid genre.")
        return None


def fetch_movie_recommendations(year):
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&primary_release_year={year}&sort_by=vote_average.desc"
    response = requests.get(url)
    data = response.json()
    # print(data)

    return parse_info(response.json(), 'recommendations')


