from typing import List
import jwt
from db.models import Session, DBUser
from sqlalchemy.sql import exists


def info_from_bearerAuth(token):
    """
    Check and retrieve authentication information from custom bearer token.
    Returned value will be passed in 'token_info' parameter of your operation function, if there is one.
    'sub' or 'uid' will be set in 'user' parameter of your operation function, if there is one.

    :param token Token provided by Authorization header
    :type token: str
    :return: Decoded token information or None if token is invalid
    :rtype: dict | None
    """
    session = Session()
    to = jwt.decode(token, options={"verify_signature": False})
    if session.query(exists().where(DBUser.userId == to['id'])).scalar() > 0:
        try:
            user = session.query(DBUser).filter(DBUser.userId == to['id']).first()
            to = jwt.decode(token, user.jwt_secret, algorithms='HS256')
            return to
        except:
            return None
    else:
        return None
    

