def add_watchlist(movie):
    try:
        with open("/Users/ryankopping/Documents/DI_Bootcamp/Week 6/Hackathon-1/Hackathon/watchlist.txt",'a') as f:
            for key,value in movie.items():
                f.write(f'{key}: {value}\n') 
            f.write('\n')
        print ('Movie saved in watchlist!')
    except Exception as e:
        print(f'Error writing to file: {e}')

def fetch_watchlist():
    try:
        with open ("/Users/ryankopping/Documents/DI_Bootcamp/Week 6/Hackathon-1/Hackathon/watchlist.txt",'r') as f:
            movies = f.readlines()
            for line in movies:
                print (line.strip())
    except Exception as e:
        print(f'Error reading from file: {e}')

def check_movie_title(title, movies):
    for movie in movies:
        if movie['Title'].lower() == title.lower():
            return movie
    