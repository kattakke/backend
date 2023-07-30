import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.api_response import ApiResponse  # noqa: E501
from openapi_server.models.book import Book  # noqa: E501
from openapi_server.models.post_book_request import PostBookRequest  # noqa: E501
from openapi_server import util

from db.models import DBBook, Session
from sqlalchemy.sql import exists


def delete_book_info(book_id):  # noqa: E501
    """delete book info

    delete book info # noqa: E501

    :param book_id: ID of book
    :type book_id: str

    :rtype: Union[ApiResponse, Tuple[ApiResponse, int], Tuple[ApiResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_book_info(book_id):  # noqa: E501
    """get book info

    get book info # noqa: E501

    :param book_id: ID of book
    :type book_id: str

    :rtype: Union[Book, Tuple[Book, int], Tuple[Book, int, Dict[str, str]]
    """
    return 'do some magic!'


def patch_book_info(book_id, post_book_request=None):  # noqa: E501
    """patch book info

    patch book info # noqa: E501

    :param book_id: ID of book
    :type book_id: str
    :param post_book_request: 
    :type post_book_request: dict | bytes

    :rtype: Union[Book, Tuple[Book, int], Tuple[Book, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        post_book_request = PostBookRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_book(post_book_request: PostBookRequest=None):  # noqa: E501
    """post book info

    post book info # noqa: E501

    :param post_book_request: 
    :type post_book_request: dict | bytes

    :rtype: Union[Book, Tuple[Book, int], Tuple[Book, int, Dict[str, str]]
    """

    # requires PostBookRequest with title, author, isbn, 
    # and adds the book to the db. (planning)

    book = {}
    book['title'] = post_book_request.title()
    book['author'] = post_book_request.author()
    book['isbn'] = post_book_request.isbn()

    session = Session()

    if session.query(exists().where(DBBook.isbn == post_book_request.isbn())).scalar() > 0:
        return (book, 500)
    else:
        dbbook = DBBook()
        dbbook.title = book['title']
        dbbook.author = book['author']
        dbbook.isbn = book['isbn']

        session.add(dbbook)
        session.commit()

    return (book, 200)

    # if connexion.request.is_json:
    #     post_book_request = PostBookRequest.from_dict(connexion.request.get_json())  # noqa: E501
    # return 'do some magic!'
