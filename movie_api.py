import requests
import random

API_KEY = '4eb1b83459cbe02d93974fbe71bae0ac'
BASE_URL = 'https://api.themoviedb.org/3'
genre_dict={28: 'Action', 12: 'Adventure', 16: 'Animation', 35: 'Comedy', 80: 'Crime', 99: 'Documentary', 18: 'Drama', 10751: 'Family', 14: 'Fantasy', 36: 'History', 27: 'Horror', 10402: 'Music', 9648: 'Mystery', 10749: 'Romance', 878: 'Science Fiction', 10770: 'TV Movie', 53: 'Thriller', 10752: 'War', 37: 'Western'}

def fetch_movie_data(movie_name):
    url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={movie_name}"
    response = requests.get(url)
    return parse_info(response.json(),'search')

def fetch_movie_by_genre(user_genre):
    genre_id=''
    for code,genre in genre_dict.items():
        if genre.lower()==user_genre:
            genre_id=code
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}"
    response = requests.get(url)
    return parse_info(response.json(),'genre')
    
def fetch_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}"
    response = requests.get(url)
    return parse_info(response.json())

def parse_info(raw_info,source):
    if raw_info['results']:
        movies=[]
        for info in raw_info['results']:
            #get just the names of the genres without the codes
            genre__names = [genre_dict[genre] for genre in info['genre_ids']]
            genre_string=', '.join(genre__names)
            movie_info = {
                'Title': info.get('title'),
                'Release_date': info.get('release_date'),
                'Overview': info.get('overview'),
                'Genres': genre_string,
                'Rating': info.get('vote_average'),
                'Number of ratings': info.get('vote_count')
            }
            movies.append(movie_info)

        if source=='search':
            return movies[0]
        elif source=='genre':
            return random.choice(movies)
    else:
        return None
 
    

