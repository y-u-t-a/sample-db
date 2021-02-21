import db
import fire
import generator
import random

class Book:
  def __init__(self, id=None, publisher_id=None, name="", author=""):
    self.id = id
    self.publisher_id = publisher_id
    self.name = name
    self.author = author

class Commands():
  def get_all_books(self):
    sql = "SELECT * FROM books"
    table = db.execute_select(sql)
    books = [Book(*row) for row in table] # タプルを展開してコンストラクタの引数に渡す
    [print(book.__dict__) for book in books]

  def register_random_book(self, count=1):
    print(f"{count} 件ランダムで books を登録します")
    publisher_list = db.execute_select("SELECT id FROM publisher")
    book_list = []
    for i in range(count):
      publisher_id = random.choice(publisher_list)[0] # SELECT の結果はタプルなので 1つ目の要素を参照する
      book_name = generator.random_book_name()
      author = generator.random_name()
      book_list.append((publisher_id, book_name, author))
    sql = "INSERT INTO books (publisher_id, name, author) VALUES (%s, %s, %s)"
    db.bulk_insert(sql, book_list)

if __name__ == '__main__':
  fire.Fire(Commands)