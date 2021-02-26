import db
import pytest

def test_DBに接続できること():
  try:
    assert db.get_connection() != None
  except:
    pytest.fail("DB接続時にエラー", False)