use library;

# マルチバイト文字を登録するための設定
SET character_set_client = utf8mb4;
SET character_set_connection = utf8mb4;

INSERT INTO publisher
  (id, name)
VALUES
  (1, '○○社'),
  (2, '△△出版'),
  (3, '□□書房')
;

INSERT INTO books
  (id, publisher_id, name, author)
VALUES
  (1, 1, 'かめこち（１）', '冬本治'),
  (2, 1, 'かめこち（２）', '冬本治'),
  (3, 2, 'おうちヨガ', 'TOSHIKI'),
  (4, 3, '１つの習慣', 'デビッド・ジャック')
;

INSERT INTO users
  (id, name, hashed_password, hash_salt)
VALUES
  ('yamada@sample.test', '山田 太郎', '1b86355f13a7f0b90c8b6053c0254399994dfbb3843e08d603e292ca13b8f672ed5e58791c10f3e36daec9699cc2fbdc88b4fe116efa7fce016938b787043818', '1b86355f13a7f0b90c8b6053c0254399994dfbb3843e08d603e292ca13b8f672ed5e58791c10f3e36daec9699cc2fbdc88b4fe116efa7fce016938b787043818'),
  ('tanaka@sample.test', '田中 花子', '5edc1c6a4390075a3ca27f4d4161c46b374b1c3b2d63f846db6fff0c513203c3ac3b14a24a6f09d8bf21407a4842113b5d9aa359d266299c3d6cf9e92db66dbe', '5edc1c6a4390075a3ca27f4d4161c46b374b1c3b2d63f846db6fff0c513203c3ac3b14a24a6f09d8bf21407a4842113b5d9aa359d266299c3d6cf9e92db66dbe')
;

INSERT INTO borrowing_history
  (user_id, book_id, start_date, limit_date, return_date)
VALUES
  ('yamada@sample.test', 1, '2020-01-10 10:30:00', '2020-01-18 00:00:00', '2020-01-15 11:00:00'),
  ('yamada@sample.test', 2, '2020-01-15 11:00:00', '2020-01-23 00:00:00', '2020-01-20 11:00:00'),
  ('tanaka@sample.test', 3, '2020-01-10 10:30:00', '2020-01-18 00:00:00', '2020-01-15 11:00:00'),
  ('tanaka@sample.test', 4, '2020-01-15 11:00:00', '2020-01-23 00:00:00', '2020-01-20 11:00:00')
;
