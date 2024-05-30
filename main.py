import json
import movie_api
import database
import recommender
from faker import Faker
import argparse
import read_write
import random

def menu():
    print('Welcome to MovieMate!')
    user_choice = input('1. Search for a movie\n2. Browse genres\n3. Filter movies by year/genre\n4. Watchlist\n5. Exit\n>')

    # Используем цикл while для проверки корректности ввода
    while user_choice not in ('1', '2', '3', '4','5'):
        print('Invalid input. Please enter a number between 1 and 5.')
        user_choice = input('1. Search for a movie\n2. Browse genres\n3. Filter movies by year/genre\n4. Watchlist\n5. Exit\n>')

    # Преобразуем пользовательский ввод в целое число для возврата
    return int(user_choice)



def movie_search(movie=None):
    if movie is None:
        movie = input('\nType the movie name\n')
    result = movie_api.fetch_movie_data(movie)
    if result:
        for key, value in result.items():
            print(f'{key}: {value}')
    
    else:
        print('No movie found. Check spelling')
    return result



def browse_genre():
    genre = input('\nType the genre you want\n')
    result = movie_api.fetch_movie_by_genre(genre)
    if result:
        counter=1
        index= random.randint(0,10)
        for movie in result[index:index+5]:
            print(f'Movie number {counter}')
            counter+=1
            for key,value in movie.items():
                print (f'{key}: {value}')
            print()
            
    else:
        print('No genre found')
    return result



        

# ----------------new mariia
def get_recommendations_by_genre_and_year():
    genre = input('\nType the genre you want\n\n')
    year = input('\nType the year you want\n\n')
    result = movie_api.fetch_movie_by_genre_and_year(genre, year)
    if result:
        index = 5
        for movie in result[:5]:
            print_movie_info(movie)

        while index < len(result):
            more = input("Do you want to see more movies? (yes/no): ").lower()
            if more == 'yes':
                for movie in result[index:index + 5]:
                    print_movie_info(movie)
                index += 5
            elif more == 'no':
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    else:
        print('No movies found for the specified genre and year.')


def get_recommendations_by_year():
    year = input('\nType the year you want\n\n')
    result = movie_api.fetch_movie_recommendations(year)
    if result:
        index = 5
        for movie in result[:5]:
            print_movie_info(movie)

        while index < len(result):
            more = input("Do you want to see more movies? (yes/no): ").lower()
            if more == 'yes':
                for movie in result[index:index + 5]:
                    print_movie_info(movie)
                index += 5
            elif more == 'no':
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    else:
        print('No recommendations found.')


def get_recommendations_by_genre():
    genre = input('\nType the genre you want\n\n')
    result = movie_api.fetch_movie_by_genre(genre)
    if result:
        index = 5
        for movie in result[:5]:
            print_movie_info(movie)

        while index < len(result):
            more = input("Do you want to see more movies? (yes/no): ").lower()
            if more == 'yes':
                for movie in result[index:index + 5]:
                    print_movie_info(movie)
                index += 5
            elif more == 'no':
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    else:
        print('No movies found for the specified genre.')


def print_movie_info(movie):
    print(f"Title: {movie['Title']}")
    print(f"Year: {movie['Release_date']}")
    print(f"Overview: {movie['Overview']}")
    print(f"Genres: {movie['Genres']}")
    print()


def main():
    user_input = menu()
    search_again='y'
    file_access=read_write()
    while user_input != 5:
        if user_input == 1:

            while search_again=='y':
                movie=movie_search()
                save = input('\nSave to watchlist?Y/N\n')
                if save.lower() == 'y':
                    file_access.add_watchlist(movie)
                search_again = input('\nSearch again? Y/N\n')
            else:
                print()
                user_input = menu()

        elif user_input == 2:
            genre_list = browse_genre()
            while search_again.lower() == 'y':
                save=input('Save a movie to watchlist? Y/N\n')
                if save.lower()=='y':
                    movie_to_save=input('What is the title of the movie you want to save?\n')
                    if file_access.check_movie_title(movie_to_save,genre_list):
                        file_access.add_watchlist(file_access.check_movie_title(movie_to_save,genre_list))
                    else:
                        movie_to_save=input('Invalid option. Enter a title from the list')
                search_again = input('\nSearch again? Y/N\n')
            else:
                print()
                user_input = menu()

        # ----------new mariia
        elif user_input == 3:
            choice = input(
                "Do you want to find movies by year, by genre or both? Enter 'year', 'genre' or 'both': ").lower()
            while choice not in ('year', 'genre', 'both'):
                choice = input("Invalid input. Please enter 'year' or 'genre': ").lower()
            else:
                if choice == 'year':
                    recommendations = get_recommendations_by_year()
                elif choice == 'genre':
                    recommendations = get_recommendations_by_genre()
                elif choice == 'both':
                    recommendations = get_recommendations_by_genre_and_year()
            if recommendations:
                for movie in recommendations:
                    print(f"Title: {movie['Title']}")
                    print(f"Year: {movie['Release_date']}")
                    print(f"Overview: {movie['Overview']}")
                    print(f"Genres: {movie['Genres']}")
                    print()
            else:
                print('No recommendations found.')

            print()
            user_input = menu()

        elif user_input==4:
            file_access.fetch_watchlist()
            print()
            user_input=menu()
            
    

    else:
        print('Thanks, come again!')
           


if __name__ == "__main__":
    main()

  

