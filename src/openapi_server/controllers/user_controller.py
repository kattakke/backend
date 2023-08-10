import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.auth_login_request import AuthLoginRequest  # noqa: E501
from openapi_server.models.book import Book  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server import util


def delete_user_info(authorization, user_id):  # noqa: E501
    """delete user info

    delete user info # noqa: E501

    :param authorization: bearer token
    :type authorization: str
    :param user_id: ID of user
    :type user_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_user_info(user_id):  # noqa: E501
    """get user info

    get user info # noqa: E501

    :param user_id: ID of user
    :type user_id: str

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_user_shelf(user_id, title=None, tag=None, isbn=None):  # noqa: E501
    """get user shelf

    get user shelf # noqa: E501

    :param user_id: ID of user
    :type user_id: str
    :param title: The title of book
    :type title: str
    :param tag: The tag of book
    :type tag: str
    :param isbn: The isbn of book
    :type isbn: str

    :rtype: Union[List[Book], Tuple[List[Book], int], Tuple[List[Book], int, Dict[str, str]]
    """
    return 'do some magic!'


def patch_user_info(authorization, user_id, auth_login_request=None):  # noqa: E501
    """patch user info

    patch user info # noqa: E501

    :param authorization: bearer token
    :type authorization: str
    :param user_id: ID of user
    :type user_id: str
    :param auth_login_request: 
    :type auth_login_request: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        auth_login_request = AuthLoginRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_register(auth_login_request=None):  # noqa: E501
    """register user

    register user # noqa: E501

    :param auth_login_request: 
    :type auth_login_request: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        auth_login_request = AuthLoginRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
