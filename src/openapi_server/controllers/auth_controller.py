import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.api_response import ApiResponse  # noqa: E501
from openapi_server.models.auth_login_request import AuthLoginRequest  # noqa: E501
from openapi_server import util


def auth_login(auth_login_request=None):  # noqa: E501
    """Returns me

    Returns me # noqa: E501

    :param auth_login_request: 
    :type auth_login_request: dict | bytes

    :rtype: Union[ApiResponse, Tuple[ApiResponse, int], Tuple[ApiResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        auth_login_request = AuthLoginRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def auth_logout():  # noqa: E501
    """logout

    logout # noqa: E501


    :rtype: Union[ApiResponse, Tuple[ApiResponse, int], Tuple[ApiResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def auth_me():  # noqa: E501
    """Returns me

    Returns me # noqa: E501


    :rtype: Union[ApiResponse, Tuple[ApiResponse, int], Tuple[ApiResponse, int, Dict[str, str]]
    """
    return 'do some magic!'
