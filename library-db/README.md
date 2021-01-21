# library-db

図書館をテーマにしたサンプルDB

## テーブル

### publisher

| Column | Primary Key | Foreign Key | Type   | Option                   |
|--------|-------------|-------------|--------|--------------------------|
| id     | TRUE        |             | 数値   | Auto Increment, Not NULL |
| name   |             |             | 文字列 | Not NULL                 |

### books

| Column       | Primary Key | Foreign Key  | Type   | Option                   |
|--------------|-------------|--------------|--------|--------------------------|
| id           | TRUE        |              | 数値   | Auto Increment, Not NULL |
| publisher_id |             | `publisher.id` | 数値   | Not NULL                 |
| name         |             |              | 文字列 | Not NULL                 |
| author       |             |              | 文字列 | Not NULL                 |

### users

| Column          | Primary Key | Foreign Key | Type   | Option   |
|-----------------|-------------|-------------|--------|----------|
| id              | TRUE        |             | 文字列 | Not NULL |
| name            |             |             | 文字列 | Not NULL |
| hashed_password |             |             | 文字列 | Not NULL |
| hash_salt       |             |             | 文字列 | Not NULL |

### borrowing_history

| Column      | Primary Key | Foreign Key | Type   | Option   |
|-------------|-------------|-------------|--------|----------|
| user_id     | TRUE        | `users.id`  | 文字列 | Not NULL |
| book_id     | TRUE        | `books.id`  | 数値   | Not NULL |
| start_date  | TRUE        |             | 日時   | Not NULL |
| limit_date  |             |             | 日時   | Not NULL |
| return_date |             |             | 日時   |          |
