"""mock_book_gen.py
generates mock book data json file.
"""
# -*- coding: utf-8 -*-

import json
import typing
import datetime
import random
import uuid

# requires mimesis
import mimesis


authors_en = [
    'Ohtani Shohei',
    'Suzuki Ichiro',
    'Niwa Koki',
]

authors_ja = [
    '大谷翔平',
    '鈴木一朗',
    '丹羽孝希',
]

class Book(object):
    def __init__(self, book_id=None, author=None, title=None, isbn=None):
        """class Book
        
        :param book_id: bookId
        :type book_id: UUID
        :param author: author of the book
        :type author: string
        :param title: title of the book
        :type title: string
        :param isbn: isbn number of the book
        :type isbn: string
        """

        self.book_id = book_id
        self.author = author
        self.title = title
        self.isbn = isbn


def generate_books(data_locale: str, n_books: int) -> typing.Iterator[Book]:

    code = mimesis.Code()
    # date = mimesis.DateTime(data_locale)
    text = mimesis.Text(data_locale)
    
    

    books = []
    for _ in range(n_books):
        book = Book(book_id=str(uuid.uuid4()))
        book.title = text.title()
        book.author = random.choice(authors_en if data_locale == 'en' else authors_ja)
        book.isbn = code.isbn()
        books.append(book)
    
    return books

def main():
    data_locale = 'ja'
    n_books = 50

    books = generate_books(data_locale, n_books=n_books)

    with open(f'books_{data_locale}.json', 'w', encoding='utf-8') as wf:
        books_ = []
        for b in books:
            book = {}
            book['book_id'] = b.book_id
            book['title'] = b.title
            book['author'] = b.author
            book['isbn'] = b.isbn
            books_.append(book)

        json.dump(books_, wf, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    main()