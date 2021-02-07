import db
import fire

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

if __name__ == '__main__':
  fire.Fire(Commands)