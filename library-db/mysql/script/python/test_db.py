import db
import pytest

def test_DBに接続できること():
  try:
    assert db.get_connection() != None
  except:
    pytest.fail("DB接続時にエラー", False)

def test_SELECT文が実行できること():
  rows = db.execute_select("SELECT * FROM books")
  assert len(rows) > 0
