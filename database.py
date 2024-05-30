import json
import sqlite3


def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn


def create_table(conn):
    sql_create_movies_table = """
    CREATE TABLE IF NOT EXISTS movies (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        release_date VARCHAR(50),
        overview TEXT,
        genres VARCHAR(255),
        rating REAL,
        number_of_ratings INTEGER
    );"""
    with conn.cursor() as cur:
        cur.execute(sql_create_movies_table)
        conn.commit()


def insert_movie(conn, movie):
    sql = ''' 
    INSERT INTO movies (title, release_date, overview, genres, rating, number_of_ratings)
    VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;
    '''
    with conn.cursor() as cur:
        cur.execute(sql, movie)
        conn.commit()
        return cur.fetchone()[0]


def fetch_all_movies(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM movies")
    rows = cur.fetchall()

    movies = []
    for row in rows:
        movie = {
            'id': row[0],
            'title': row[1],
            'details': json.loads(row[2])
        }
        movies.append(movie)

    return movies

if __name__ == "__main__":
    db_config = {
        'dbname': 'top_movies',
        'user': 'postgres',
        'password': '',
        'host': 'localhost',
        'port': 5432
    }
    conn = create_connection(db_config)
    create_table(conn)
