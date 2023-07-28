import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.api_response import ApiResponse
from openapi_server.models.auth_login_request import AuthLoginRequest
from openapi_server.models.post_book_request import PostBookRequest  # noqa: E501
from openapi_server import util

from openapi_server.models.post_book_request import PostBookRequest

from db.models import Session, DBBook
from sqlalchemy.sql import exists


def get_search_book(title: str=None, isbn: str=None):  # noqa: E501
    """search book

    search book # noqa: E501

    :param title: The title of book
    :type title: str
    :param isbn: The isbn of book
    :type isbn: str

    :rtype: Union[PostBookRequest, Tuple[PostBookRequest, int], Tuple[PostBookRequest, int, Dict[str, str]]
    """

    # search book from isbn

    # create session
    session = Session()


    # check if book which has that isbn exists...
    if session.query(exists().where(DBBook.isbn == isbn)).scalar() > 0:
        # print("本あったよ")
        books = session.query(DBBook.query.filter(DBBook.isbn == isbn)).all()
        for book in books:
            # return PostBookRequest with the isbn, title, and author
            return (PostBookRequest(isbn=isbn, title=book.title, author=book.author), 200)
    else:
        # print("本なかったよ泣")
        return (PostBookRequest(isbn=None, title=None, author=None), 500)