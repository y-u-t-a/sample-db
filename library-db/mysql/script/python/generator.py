import random
import string
import os

def file_to_list(file_path: string):
    with open(file_path) as input_file:
        return [ word.replace(os.linesep, '') for word in input_file.readlines() ]

FIRST_NAMES = file_to_list(f"{os.path.dirname(__file__)}/../data/first_names.txt")
LAST_NAMES = file_to_list(f"{os.path.dirname(__file__)}/../data/last_names.txt")
BOOK_NAME_FIRST = file_to_list(f"{os.path.dirname(__file__)}/../data/book_name_first.txt")
BOOK_NAME_SECOND = file_to_list(f"{os.path.dirname(__file__)}/../data/book_names_second.txt")

def random_name():
    return random.choice(LAST_NAMES) + random.choice(FIRST_NAMES)

def random_book_name():
    return random.choice(BOOK_NAME_FIRST) + random.choice(BOOK_NAME_SECOND)

def random_email_address():
    source = string.ascii_lowercase + string.digits
    # email を varchar(200) で定義していて、ドメイン部分を 12 文字で固定しているため最大の長さは 188
    length = random.choice(range(5, 188))
    return ''.join(random.choices(source, k=length)) + "@sample.test"