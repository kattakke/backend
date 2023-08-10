import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.auth_login_request import AuthLoginRequest  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server import util

from db.models import Session, DBUser
import bcrypt
from sqlalchemy.sql import exists
import secrets
import jwt


def auth_login(auth_login_request=None):  # noqa: E501
    """get authorize token

    get authorize token # noqa: E501

    :param auth_login_request: 
    :type auth_login_request: dict | bytes

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
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
            return token
    else:
        return None, 401


def auth_logout(authorization = None, token_info = None):  # noqa: E501
    """logout

    delete token # noqa: E501

    :param authorization: bearer token
    :type authorization: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    session = Session()
    if session.query(exists().where(DBUser.userId == token_info['id'])).scalar() > 0:
        user = session.query(DBUser).filter(DBUser.userId == token_info['id']).first()
        user.jwt_secret = ""
        session.commit()
    
    return None


def auth_me(authorization = None, token_info = None):  # noqa: E501
    """Returns me

    get authrized user info # noqa: E501

    :param authorization: bearer token
    :type authorization: str

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    session = Session()
    if session.query(exists().where(DBUser.userId == token_info['id'])).scalar() > 0:
        user = session.query(DBUser).filter(DBUser.userId == token_info['id']).first()
        return User(user_id=user.userId, name=user.name, shelf=user.shelf)