import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.book import Book  # noqa: E501
from openapi_server.models.post_book_request import PostBookRequest  # noqa: E501
from openapi_server import util

from db.models import Session, DBBook, DBShelf
from sqlalchemy.sql import exists

def delete_book_info(authorization = None, book_id = None):  # noqa: E501
    """delete book info

    delete book info # noqa: E501

    :param authorization: bearer token
    :type authorization: str
    :param book_id: ID of book
    :type book_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """

    session = Session()
    if session.query(exists().where(DBShelf.book == book_id)).scalar() > 0:
            book = session.query(DBShelf).filter(DBShelf.book == book_id).first()
            session.delete(book)
            session.commit()
    else:
        return None, 400
    if session.query(exists().where(DBBook.bookId == book_id)).scalar() > 0:
            book = session.query(DBBook).filter(DBBook.bookId == book_id).first()
            session.delete(book)
            session.commit()
    else:
        return None, 400
    return None, 200


def get_book_info(book_id):  # noqa: E501
    """get book info

    get book info # noqa: E501

    :param book_id: ID of book
    :type book_id: str

    :rtype: Union[Book, Tuple[Book, int], Tuple[Book, int, Dict[str, str]]
    """
    session = Session()
    if session.query(exists().where(DBBook.bookId == book_id)).scalar() > 0:
            book = session.query(DBBook).filter(DBBook.bookId == book_id).first()
            return Book(book_id= str(book.bookId), isbn= book.isbn, title = book.title, author= book.author, image_path = book.imagePath)
    else:
        return None, 404

def patch_book_info(authorization = None, book_id = None, token_info = None, post_book_request=None):  # noqa: E501
    """patch book info

    patch book info # noqa: E501

    :param authorization: bearer token
    :type authorization: str
    :param book_id: ID of book
    :type book_id: str
    :param post_book_request: 
    :type post_book_request: dict | bytes

    :rtype: Union[Book, Tuple[Book, int], Tuple[Book, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        post_book_request = PostBookRequest.from_dict(connexion.request.get_json())  # noqa: E501
    session = Session()
    if session.query(exists().where(DBBook.bookId == book_id)).scalar() > 0:
            book = session.query(DBBook).filter(DBBook.bookId == book_id).first()
            book.isbn = post_book_request.isbn
            book.title = post_book_request.title
            book.author = post_book_request.author
            book.imagePath = post_book_request.image_path
            session.commit()
            return Book(book_id= str(book.bookId), isbn= book.isbn, title = book.title, author= book.author, image_path=book.imagePath)
    else:
        return None, 404
    


def post_book(authorization = None, post_book_request=None, token_info = None):  # noqa: E501
    """post book info

    post book info # noqa: E501

    :param authorization: bearer token
    :type authorization: str
    :param post_book_request: 
    :type post_book_request: dict | bytes

    :rtype: Union[Book, Tuple[Book, int], Tuple[Book, int, Dict[str, str]]
    """

    # requires PostBookRequest with title, author, isbn, 
    # and adds the book to the db. (planning)

    if connexion.request.is_json:
        post_book_request = PostBookRequest.from_dict(connexion.request.get_json())  # noqa: E501

    session = Session()

    book = DBBook()
    book.isbn = post_book_request.isbn
    book.title = post_book_request.title
    book.author = post_book_request.author
    book.imagePath = post_book_request.image_path
    session.add(book)
    session.commit()

    shelf = DBShelf()
    shelf.shelfId = token_info["shelf"]
    shelf.book = book.bookId
    session.add(shelf)
    session.commit()
    return Book(book_id= str(book.bookId), isbn= book.isbn, title = book.title, author= book.author, image_path=book.imagePath)

