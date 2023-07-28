import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.api_response import ApiResponse  # noqa: E501
from openapi_server.models.auth_login_request import AuthLoginRequest  # noqa: E501
from openapi_server import util

from db.models import Session, DBUser
import bcrypt
from sqlalchemy.sql import exists
import secrets
import jwt


def auth_login(auth_login_request=None):  # noqa: E501
    """Returns me

    Returns me # noqa: E501

    :param auth_login_request: 
    :type auth_login_request: dict | bytes

    :rtype: Union[ApiResponse, Tuple[ApiResponse, int], Tuple[ApiResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        auth_login_request = AuthLoginRequest.from_dict(connexion.request.get_json())  # noqa: E501
    
    session = Session()
    if session.query(exists().where(DBUser.name == auth_login_request.id)).scalar() > 0:
        user = session.query(DBUser).filter(DBUser.name == auth_login_request.id).first()
        if bcrypt.checkpw(auth_login_request.password.encode('utf8'), user.password.encode('utf8')):
            user.jwt_secret = secrets.token_urlsafe(16)
            session.commit()
            payload = {
                "id": str(user.userId),
                "name": user.name,
                "shelf": str(user.shelf),
                "permission": "User"
            }
            token = jwt.encode(payload, user.jwt_secret)
            return ApiResponse(code="200", type="string", message=token)
    else:
        return ApiResponse(code="401", type="string", message="Unauthorized"), 401


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
