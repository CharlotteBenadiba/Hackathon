import json
import movie_api
import database
import recommender
from faker import Faker
import argparse

def menu():

    print('Welcome to MovieMate!')
    user_choice=input('1.Search for a movie\n2.Browse genres\n3.Get recommendations\n4.Exit\n>')
    while user_choice not in ('1234'):
        user_choice=('Invalid input')
    else:
        if user_choice=='1':
            return 1
        elif user_choice=='2':
            return 2
        elif user_choice=='3':
            return 3
        elif user_choice=='4':
            return 4
        
def movie_search():
    movie=input('\nType the movie name\n\n')
    result=movie_api.fetch_movie_data(movie)
    return result

def browse_genre ():
    genre=input('\nType the genre you want\n\n')
    result = movie_api.fetch_movie_by_genre(genre)
    return result

#Need to add in the database code
def watchlist(search_movie):
    query=(f'insert into watchlist values{search_movie}')
    print ('Success')
    
    
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


    user_input=menu()
    search_again='y'
    while user_input != 4:
        if user_input==1:
            while search_again!='n':
                movie=movie_search()
                if movie is not None:
                    if movie is not None:
                        for key,value in movie.items():
                            print(f'{key}: {value}')
                    else:
                        print('No movie found. Check spelling')

                save = input('\nSave to watchlist?Y/N\n')
                if save.lower()=='y':
                    watchlist(movie)
                search_again = input('\nSearch again? Y/N\n')
            
            # while search_again.lower()=='y':
            #     print()
            #     movie_search()
            #     search_again=input('\nSearch again? Y/N\n')
            else: 
                print()
                user_input=menu()
                
        elif user_input==2:
            genre_list=browse_genre()

            if genre_list is not None:
              
                for key,value in genre_list.items():
                        print(f'{key}: {value}')
                
            else:
                print('No genre found. Check spelling')

            search_again = input('\nSearch again? Y/N\n')
            while search_again.lower()=='y':
                print()
                genre_list=browse_genre()
                search_again=input('\nSearch again? Y/N\n')
            else:
                print()
                user_input=menu()
      
    else:
        print('Thanks, come again!')




if __name__ == "__main__":
    main()
