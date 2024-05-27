import json
import movie_api
import database
import recommender
from faker import Faker
import argparse

def menu():
    print('Welcome to MovieMate!')
    user_choice=input('1.Search for a movie\n2.Browse genres\n3.Get recommendations\n4.Exit\n')
    if user_choice=='1':
        movie=input('Type the movie name\n')
        movie_search(movie)
    elif user_choice==2:
        genre=input('What genre do you want to find?\n')
        find_genre(genre)
    elif user_choice==3:
        genre=input('What genre do you feel like watching? You can choose up to 3 genres\n')
    elif user_choice==4:
        print('See you soon!')
    else:
        user_input=('Invalid input')







def movie_search(movie_name):
    #Need to update query based on what data we should show
    query=(f'select * from top_movies where title like {movie_name} limit 3')
    return query

def find_genre (genre):
    query=(f'select * from movies where genre like {genre} limit 3')
    return query





def main():
    # # Инициализация базы данных
    # conn = database.create_connection('movies.db')
    # database.create_table(conn)

    # # Получение данных о фильмах и их сохранение
    # movie_data = movie_api.fetch_movie_data('Inception')
    # for movie in movie_data['results']:
    #     movie_details = movie_api.fetch_movie_details(movie['id'])
    #     database.insert_movie(conn, (movie['id'], movie['title'], json.dumps(movie_details)))

    # # Загрузка всех фильмов из базы данных
    # all_movies = database.fetch_all_movies(conn)

    # # Генерация тестовых данных пользователей
    # fake = Faker()
    # user_preferences = {'genres': [fake.word() for _ in range(3)]}

    # # Рекомендация фильмов
    # recommendations = recommender.recommend_movies(user_preferences, all_movies)
    # print(f"Recommendations for user with preferences {user_preferences}:")
    # for rec in recommendations:
    #     print(rec)


    menu()


if __name__ == "__main__":
    main()
