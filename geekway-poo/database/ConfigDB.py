import psycopg2
import mysql.connector

config = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'geekway',
  'raise_on_warnings': True
}

DB_NAME = 'GeekWay'
DB_USER = 'postgres'
DB_PASSWORD = 'rennanbd'

def connectar():
    #return psycopg2.connect("dbname=%s user=%s password=%s" % (DB_NAME, DB_USER, DB_PASSWORD))
    return mysql.connector.connect(**config)