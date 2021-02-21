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

def bulk_insert(insert_query:str, values:list):
  """
  ```python
  query = "INSERT INTO employees (name, phone) VALUES (%s, %s)"
  data = [
    ('Jane','555-001'),
    ('Joe', '555-001'),
    ('John', '555-003')
  ]
  db.bulk_insert(query, data)
  ```
  """
  with get_connection() as conection:
    with conection.cursor() as cursor:
      cursor.executemany(insert_query, values)
    conection.commit()