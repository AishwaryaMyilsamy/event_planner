import psycopg2
from psycopg2 import sql

def get_connection():
    return psycopg2.connect(
        dbname='event_planner',
        user='postgres', 
        password='postgres', 
        host='localhost',
        port='5432'
    )

def initialize_db():
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS venues (
            id SERIAL PRIMARY KEY,
            name TEXT,
            location TEXT,
            type TEXT,
            price INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def add_venue(name, location, type, price):
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        INSERT INTO venues (name, location, type, price)
        VALUES (%s, %s, %s, %s)
    ''', (name, location, type, price))
    conn.commit()
    conn.close()

def get_venues(location, max_price, type=None):
    conn = get_connection()
    c = conn.cursor()
    query = 'SELECT * FROM venues WHERE location = %s AND price <= %s'
    params = [location, max_price]
    if type:
        query += ' AND type = %s'
        params.append(type)
    c.execute(query, params)
    venues = c.fetchall()
    conn.close()
    return venues
