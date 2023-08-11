import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.book_search import BookSearch  # noqa: E501
from openapi_server import util

from openapi_server.models.book import Book

from db.models import Session, DBBook
from sqlalchemy.sql import exists

import requests

def get_search_book(title: str=None, isbn: str=None):  # noqa: E501
    """search book

    search book # noqa: E501

    :param title: The title of book
    :type title: str
    :param isbn: The isbn of book
    :type isbn: str

    :rtype: Union[List[BookSearch], Tuple[List[BookSearch], int], Tuple[List[BookSearch], int, Dict[str, str]]
    """


    if not title == None:
        url = f'https://www.googleapis.com/books/v1/volumes?q={title}'
        r = requests.get(url)

        items = r.json()['items']
        books = []
        for book_ in items:
            title_ = book_['volumeInfo']['title']
            isbn_ = ""
            author_ = ""
            image_path_ = ""
            if 'industryIdentifiers' in book_['volumeInfo']:
                isbn_ = book_['volumeInfo']['industryIdentifiers'][0]['identifier']
            if 'authors' in book_['volumeInfo']:
                author_ = book_['volumeInfo']['authors'][0]
            if 'imageLinks' in book_['volumeInfo']:
                image_path_ = book_['volumeInfo']['imageLinks']['thumbnail']
            books.append(BookSearch(isbn=isbn_, title=title_, author=author_, image_path=image_path_))

        # return (PostBookRequest(isbn=books[0]['isbn'], title=books[0]['title'], author=books[0]['author']), 200)
        return (books, 200)
    if not isbn == None:
        url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}'
        # search book from isbn

        r = requests.get(url)
        items = r.json()['items']
        books = []
        for book_ in items:
            title_ = book_['volumeInfo']['title']
            isbn_ = ""
            author_ = ""
            image_path_ = ""
            if 'industryIdentifiers' in book_['volumeInfo']:
                isbn_ = book_['volumeInfo']['industryIdentifiers'][0]['identifier']
            if 'authors' in book_['volumeInfo']:
                author_ = book_['volumeInfo']['authors'][0]
            if 'imageLinks' in book_['volumeInfo']:
                image_path_ = book_['volumeInfo']['imageLinks']['thumbnail']
            books.append(BookSearch(isbn=isbn_, title=title_, author=author_, image_path=image_path_))
        return (books, 200)
    # if session.query(exists().where(DBBook.isbn == isbn)).scalar() > 0:
    #     # print("本あったよ")
    #     books = session.query(DBBook.query.filter(DBBook.isbn == isbn)).all()
    #     for book in books:
    #         # return PostBookRequest with the isbn, title, and author
    #         return (PostBookRequest(isbn=isbn, title=book.title, author=book.author), 200)
    # else:
    #     # print("本なかったよ泣")
    #     return (PostBookRequest(isbn=None, title=None, author=None), 400)