import mysql.connector
import os

def get_connection():
  db_host = os.getenv("DB_HOST", "localhost")
  return mysql.connector.connect(
      host = db_host,
      port = 3306,
      user = "root",
      password = "root",
      database = "library"
  )

def execute_select(query:str):
  with get_connection() as conection:
    with conection.cursor() as cursor:
      cursor.execute(query)
      return cursor.fetchall()
