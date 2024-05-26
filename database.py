import json
import sqlite3


def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn


def create_table(conn):
    sql_create_movies_table = """
    CREATE TABLE IF NOT EXISTS movies (
        id integer PRIMARY KEY,
        title text NOT NULL,
        details text NOT NULL
    );"""
    conn.execute(sql_create_movies_table)
    conn.commit()


def insert_movie(conn, movie):
    sql = ''' INSERT INTO movies(id, title, details)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, movie)
    conn.commit()
    return cur.lastrowid


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
