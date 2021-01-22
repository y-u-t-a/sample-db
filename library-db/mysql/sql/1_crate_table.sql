use library;

CREATE TABLE publisher (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  name VARCHAR(200) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE books (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  publisher_id INT UNSIGNED,
  name VARCHAR(800),
  author VARCHAR(400),
  PRIMARY KEY (id),
  FOREIGN KEY (publisher_id)
    REFERENCES publisher(id)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);

CREATE TABLE users (
  id VARCHAR(200) NOT NULL,
  name VARCHAR(200) NOT NULL,
  hashed_password VARCHAR(512) NOT NULL,
  hash_salt VARCHAR(512) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE borrowing_history(
  user_id VARCHAR(200) NOT NULL,
  book_id INT UNSIGNED NOT NULL,
  start_date DATETIME NOT NULL,
  limit_date DATETIME NOT NULL,
  return_date DATETIME,
  PRIMARY KEY (user_id, book_id, start_date),
  FOREIGN KEY (user_id)
    REFERENCES users(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  FOREIGN KEY (book_id)
    REFERENCES books(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);