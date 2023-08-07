import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.api_response import ApiResponse
from openapi_server.models.auth_login_request import AuthLoginRequest
from openapi_server.models.post_book_request import PostBookRequest  # noqa: E501
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

    :rtype: Union[Book, Tuple[Book, int], Tuple[Book, int, Dict[str, str]]
    """


    if not title == None:
        url = f'https://www.googleapis.com/books/v1/volumes?q={title}'
        r = requests.get(url)

        book_= r.json()['items'][0]

        # books = []
        title_ = book_['volumeInfo']['title']
        isbn_ = book_['volumeInfo']['industryIdentifiers'][0]['identifier']
        author_ = book_['volumeInfo']['authors'][0]
        image_path_ = book_['volumeInfo']['imageLinks']['thumbnail']
        # books.append({'title': title_, 'isbn': isbn_, 'author': author_})

        # return (PostBookRequest(isbn=books[0]['isbn'], title=books[0]['title'], author=books[0]['author']), 200)
        return (Book(isbn=isbn_, title=title_, author=author_, image_path=image_path_), 200)
    if not isbn == None:
        url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}'
        # search book from isbn

        r = requests.get(url)
        book_ = r.json()['items'][0]

        title_ = book_['volumeInfo']['title']
        isbn_ = book_['volumeInfo']['industryIdentifiers'][0]['identifier']
        author_  = book_['volumeInfo']['authors'][0]
        image_path_ = book_['volumeInfo']['imageLinks']['thumbnail']
        return (Book(isbn=isbn, title=title_, author=author_, image_path=image_path_), 200)
    # if session.query(exists().where(DBBook.isbn == isbn)).scalar() > 0:
    #     # print("本あったよ")
    #     books = session.query(DBBook.query.filter(DBBook.isbn == isbn)).all()
    #     for book in books:
    #         # return PostBookRequest with the isbn, title, and author
    #         return (PostBookRequest(isbn=isbn, title=book.title, author=book.author), 200)
    # else:
    #     # print("本なかったよ泣")
    #     return (PostBookRequest(isbn=None, title=None, author=None), 400)