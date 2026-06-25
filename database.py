import psycopg2
def get_db():
    conn=psycopg2.connect(
        host='localhost',
        database='TestAPI',
        user='postgres',
        password='lion')
    return conn

