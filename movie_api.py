import requests

API_KEY = '4eb1b83459cbe02d93974fbe71bae0ac'
BASE_URL = 'https://api.themoviedb.org/3'

def fetch_movie_data(movie_name):
    url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={movie_name}"
    response = requests.get(url)
    return parse_info(response.json())
    
def fetch_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}"
    response = requests.get(url)
    return parse_info(response.json())

def parse_info(raw_info):
    if raw_info['results']:
        first_result = raw_info['results'][0]

        #creates dictionary of the genres
        genre_dict={28: 'Action', 12: 'Adventure', 16: 'Animation', 35: 'Comedy', 80: 'Crime', 99: 'Documentary', 18: 'Drama', 10751: 'Family', 14: 'Fantasy', 36: 'History', 27: 'Horror', 10402: 'Music', 9648: 'Mystery', 10749: 'Romance', 878: 'Science Fiction', 10770: 'TV Movie', 53: 'Thriller', 10752: 'War', 37: 'Western'}
        #get just the names of the genres without the codes
        genre__names = [genre_dict[genre] for genre in first_result['genre_ids']]
        #format the genres to display nicely
        genre_string=', '.join(genre__names)

        #format the info for the movie so it is more readable
        movie_info = {
            'Title': first_result.get('title'),
            'Release_date': first_result.get('release_date'),
            'Overview': first_result.get('overview'),
            'Genres': genre_string,
            'Rating': first_result.get('vote_average'),
            'Number of ratings': first_result.get('vote_count')
        }
        return movie_info
    else:
        return None
 
    

