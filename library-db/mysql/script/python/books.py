import db
import fire

class Book:
  def __init__(self, id=None, publisher_id=None, name="", author=""):
    self.id = id
    self.publisher_id = publisher_id
    self.name = name
    self.author = author

  def to_dict(self):
    return {
      "id": self.id,
      "publisher_id": self.publisher_id,
      "name": self.name,
      "author": self.author
    }

class Commands():
  def get_all_books(self):
    sql = "SELECT * FROM books"
    table = db.execute_select(sql)
    books = [Book(*row) for row in table] # タプルを展開してコンストラクタの引数に渡す
    [print(book.to_dict()) for book in books]

if __name__ == '__main__':
  fire.Fire(Commands)