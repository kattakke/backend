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


    # the same function available more simply with `filtered_by()`
    # but not preferred in team development.
    (book, code) = get_book_info(book_id)

    if code == 200:
        session = Session()
        the_book = session.query(DBBook).filter(DBBook.bookId == book_id).first()
        session.delete(the_book)
    elif code == 500:
        return ApiResponse(code="500", type="string", message="book not found")
    
    return ApiResponse(code="200", type="string", message="OK")
    # return 'do some magic!'


def get_book_info(book_id):  # noqa: E501
    """get book info

    get book info # noqa: E501

    :param book_id: ID of book
    :type book_id: str

    :rtype: Union[Book, Tuple[Book, int], Tuple[Book, int, Dict[str, str]]
    """

    book = Book()
    session = Session()

    if session.query(exists().where(DBBook.bookId == book_id)).scalar() > 0:
        dbbook = DBBook()
        the_book = session.query(DBBook).filter(DBBook.bookId == book_id).first()
        book.title = the_book.title
        book.author = the_book.author
        book.isbn = the_book.isbn
        return (book, 200)
    else:
        book.title = None
        book.author = None
        book.isbn = None
        
        return (book, 500)
    # return 'do some magic!'


def patch_book_info(book_id, post_book_request: PostBookRequest=None):  # noqa: E501
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


def post_book(post_book_request=None):  # noqa: E501
    """post book info

    post book info # noqa: E501

    :param post_book_request: 
    :type post_book_request: dict | bytes

    :rtype: Union[Book, Tuple[Book, int], Tuple[Book, int, Dict[str, str]]
    """

    # requires PostBookRequest with title, author, isbn, 
    # and adds the book to the db. (planning)

    if connexion.request.is_json:
        post_book_request = PostBookRequest.from_dict(connexion.request.get_json())  # noqa: E501

    book = Book(title=None, isbn=None, author=None)
    session = Session()

    # if both 'book' and 'post_book_request' are None,
    # returns None (hence {}) and code 500 instead.
    # if any attribute of post_book_request is None,
    # returns book with "... not specified" and code 200 instead.
    # if the same book exists on the db,
    # returns book and code 500.
    if not post_book_request == None:
        book.title = post_book_request.title() or "title not specified"
        book.author = post_book_request.author() or "author not specified"
        book.isbn = post_book_request.isbn() or "isbn not specified"
        if session.query(exists().where(DBBook.isbn == post_book_request.isbn())).scalar() > 0:
            # print('the book already exists on db')
            return (book, 500)
        else:
            dbbook = DBBook()
            dbbook.title = book.title
            dbbook.author = book.author
            dbbook.isbn = book.isbn

            session.add(dbbook)
            session.commit()
            return (book, 200)
    else:
        return (book, 500)

    # if connexion.request.is_json:
    #     post_book_request = PostBookRequest.from_dict(connexion.request.get_json())  # noqa: E501
    # return 'do some magic!'
