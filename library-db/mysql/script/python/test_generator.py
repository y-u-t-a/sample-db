import generator

def test_ランダムな人名を生成できること():
  random_name = generator.random_name()
  # LAST_NAME + FIRST_NAME で少なくとも2文字以上になる
  assert len(random_name) >= 2

def test_10回ランダムな人名を生成して重複がないこと():
  name_list = []
  for i in range(10):
    name_list.append(generator.random_name())
  duplicated_list = [x for x in set(name_list) if name_list.count(x) > 1]
  assert len(duplicated_list) == 0

def test_ランダムな書籍名を生成できること():
  random_book_name = generator.random_book_name()
  # 上の句 + 下の句 で少なくとも2文字以上になる
  assert len(random_book_name) >= 2

def test_ランダムな書籍名を10回生成して重複がないこと():
  book_name_list = []
  for i in range(10):
    book_name_list.append(generator.random_book_name())
  # list を set に変換し、set 内の出現回数が 1 より大きい要素を抽出する
  duplicated_list = [x for x in set(book_name_list) if book_name_list.count(x) > 1]
  assert len(duplicated_list) == 0

def test_ランダムなemailを生成できること():
  random_email = generator.random_email_address()
  assert random_email.endswith('@sample.test')
  assert len(random_email) >= 17 # 固定文字列 + ランダム文字列の最小の長さ
  assert len(random_email) <= 200 # 固定文字列 + ランダム文字列の最大の長さ

def test_ランダムなemailを10回生成して重複がないこと():
  email_list = []
  for i in range(10):
    email_list.append(generator.random_email_address())
  duplicated_list = [x for x in set(email_list) if email_list.count(x) > 1]
  assert len(duplicated_list) == 0
