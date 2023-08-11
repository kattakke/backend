import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.book_search import BookSearch  # noqa: E501
from openapi_server import util


def get_search_book(title=None, isbn=None):  # noqa: E501
    """search book

    search book # noqa: E501

    :param title: The title of book
    :type title: str
    :param isbn: The isbn of book
    :type isbn: str

    :rtype: Union[List[BookSearch], Tuple[List[BookSearch], int], Tuple[List[BookSearch], int, Dict[str, str]]
    """
    return 'do some magic!'
