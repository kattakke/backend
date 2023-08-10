import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.book import Book  # noqa: E501
from openapi_server.models.post_book_request import PostBookRequest  # noqa: E501
from openapi_server import util


def delete_book_info(authorization, book_id):  # noqa: E501
    """delete book info

    delete book info # noqa: E501

    :param authorization: bearer token
    :type authorization: str
    :param book_id: ID of book
    :type book_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
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


def patch_book_info(authorization, book_id, post_book_request=None):  # noqa: E501
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
    return 'do some magic!'


def post_book(authorization, post_book_request=None):  # noqa: E501
    """post book info

    post book info # noqa: E501

    :param authorization: bearer token
    :type authorization: str
    :param post_book_request: 
    :type post_book_request: dict | bytes

    :rtype: Union[Book, Tuple[Book, int], Tuple[Book, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        post_book_request = PostBookRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
