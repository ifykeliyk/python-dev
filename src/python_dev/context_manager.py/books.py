import sqlite3

books = [
    (1, 'To Kill a Mockingbird'),
    (2, 'Catcher in the Rye'),
    (3, 'The Great Gatsby'),
    (4, '1984'),
    (5, 'Pride and Prejudice'),
]

with sqlite3.connect('library.db') as conn:
    cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT)')
    for book in books:
        cursor.execute('INSERT INTO books VALUES (?, ?)', book)
