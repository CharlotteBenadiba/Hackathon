import json
import movie_api
import database
import recommender
from faker import Faker


def main():
    # Инициализация базы данных
    conn = database.create_connection('movies.db')
    database.create_table(conn)

    # Получение данных о фильмах и их сохранение
    movie_data = movie_api.fetch_movie_data('Inception')
    for movie in movie_data['results']:
        movie_details = movie_api.fetch_movie_details(movie['id'])
        database.insert_movie(conn, (movie['id'], movie['title'], json.dumps(movie_details)))

    # Загрузка всех фильмов из базы данных
    all_movies = database.fetch_all_movies(conn)

    # Генерация тестовых данных пользователей
    fake = Faker()
    user_preferences = {'genres': [fake.word() for _ in range(3)]}

    # Рекомендация фильмов
    recommendations = recommender.recommend_movies(user_preferences, all_movies)
    print(f"Recommendations for user with preferences {user_preferences}:")
    for rec in recommendations:
        print(rec)


if __name__ == "__main__":
    main()
