def matches_preferences(movie, user_preferences):
    movie_genres = [genre['name'] for genre in movie['details']['genres']]
    for genre in movie_genres:
        if genre in user_preferences['genres']:
            return True
    return False

def recommend_movies(user_preferences, all_movies):
    recommended_movies = []
    for movie in all_movies:
        if matches_preferences(movie, user_preferences):
            recommended_movies.append(movie['title'])
    return recommended_movies
