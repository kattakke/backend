import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.auth_login_request import AuthLoginRequest  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server import util


def auth_login(auth_login_request=None):  # noqa: E501
    """get authorize token

    get authorize token # noqa: E501

    :param auth_login_request: 
    :type auth_login_request: dict | bytes

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        auth_login_request = AuthLoginRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def auth_logout(authorization):  # noqa: E501
    """delete token

    delete token # noqa: E501

    :param authorization: bearer token
    :type authorization: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def auth_me(authorization):  # noqa: E501
    """get authrized user info

    get authrized user info # noqa: E501

    :param authorization: bearer token
    :type authorization: str

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    return 'do some magic!'
