import json
import movie_api
import database
import recommender
from faker import Faker
import argparse


def menu():
    print('Welcome to MovieMate!')
    user_choice = input('1. Search for a movie\n2. Browse genres\n3. Filter movies by year/genre\n4. Exit\n>')

    # Используем цикл while для проверки корректности ввода
    while user_choice not in ('1', '2', '3', '4'):
        print('Invalid input. Please enter a number between 1 and 4.')
        user_choice = input('1. Search for a movie\n2. Browse genres\n3. Filter movies by year/genre\n4. Exit\n>')

    # Преобразуем пользовательский ввод в целое число для возврата
    return int(user_choice)
    #
    #
    # print('Welcome to MovieMate!')
    # user_choice=input('1.Search for a movie\n2.Browse genres\n3.Filter movis by year/genre\n4.Exit\n>')
    # #     user_choice=input('1.Search for a movie\n2.Browse genres\n3.Get recommendations\n4.Exit\n>')
    # while user_choice not in ('1234'):
    #     user_choice=('Invalid input')
    # else:
    #     if user_choice=='1':
    #         return 1
    #     elif user_choice=='2':
    #         return 2
    #     elif user_choice=='3':
    #         return 3
    #     elif user_choice=='4':
    #         return 4
    #


def movie_search():
    movie = input('\nType the movie name\n\n')
    result = movie_api.fetch_movie_data(movie)
    return result


def browse_genre():
    genre = input('\nType the genre you want\n\n')
    result = movie_api.fetch_movie_by_genre(genre)
    return result


# Need to add in the database code
def watchlist(search_movie):
    query = (f'insert into watchlist values{search_movie}')
    print('Success')


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
    while user_input != 4:
        if user_input == 1:
            movie = movie_search()
            if movie is not None:
                if movie is not None:
                    for key, value in movie.items():
                        print(f'{key}: {value}')
                else:
                    print('No movie found. Check spelling')

            save = input('\nSave to watchlist?Y/N\n')
            if save.lower() == 'y':
                watchlist(movie)
            search_again = input('\nSearch again? Y/N\n')
            while search_again.lower() == 'y':
                print()
                movie_search()
                search_again = input('\nSearch again? Y/N\n')
            else:
                print()
                user_input = menu()

        elif user_input == 2:
            genre_list = browse_genre()

            if genre_list is not None:

                for key, value in genre_list.items():
                    print(f'{key}: {value}')

            else:
                print('No genre found. Check spelling')

            search_again = input('\nSearch again? Y/N\n')
            while search_again.lower() == 'y':
                print()
                genre_list = browse_genre()
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

        else:
            print('Thanks, come again!')
            break

    else:
        print('Thanks, come again!')


if __name__ == "__main__":
    main()
