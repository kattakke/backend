import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.api_response import ApiResponse  # noqa: E501
from openapi_server.models.auth_login_request import AuthLoginRequest  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server import util
from db.models import Session, DBUser, DBBook, DBShelf
import bcrypt
from sqlalchemy.sql import exists

def delete_user_info(user_id):  # noqa: E501
    """delete user info

    delete user info # noqa: E501

    :param user_id: ID of user
    :type user_id: str

    :rtype: Union[ApiResponse, Tuple[ApiResponse, int], Tuple[ApiResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_user_info(user_id):  # noqa: E501
    """get user info

    get user info # noqa: E501

    :param user_id: ID of user
    :type user_id: str

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    session = Session()
    if session.query(exists().where(DBUser.userId == user_id)).scalar() > 0:
        user = session.query(DBUser).filter(DBUser.userId == user_id).first()
        return User(user_id=str(user.userId), name = user.name, shelf=user.shelf)
    else:
        return (ApiResponse(code="404", type="string", message="Not Found"), 404)
    


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

    :rtype: Union[List[str], Tuple[List[str], int], Tuple[List[str], int, Dict[str, str]]
    """
    session = Session()
    if session.query(exists().where(DBUser.userId == user_id)).scalar() > 0:
        user = session.query(DBUser).filter(DBUser.userId == user_id).first()
        shelf = user.shelf
        books = session.query(DBShelf).filter(DBShelf.shelfId==shelf).all()
        l = []
        for i in books:
            l.append(str(i.book))
        return l

        
    else:
        return (ApiResponse(code="404", type="string", message="Not Found"), 404)
         


def patch_user_info(user_id):  # noqa: E501
    """patch user info

    patch user info # noqa: E501

    :param user_id: ID of user
    :type user_id: str

    :rtype: Union[ApiResponse, Tuple[ApiResponse, int], Tuple[ApiResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def user_register(auth_login_request=None):  # noqa: E501
    """register

    register # noqa: E501

    :param auth_login_request: 
    :type auth_login_request: dict | bytes

    :rtype: Union[ApiResponse, Tuple[ApiResponse, int], Tuple[ApiResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        auth_login_request = AuthLoginRequest.from_dict(connexion.request.get_json())  # noqa: E501
    session = Session()
    if session.query(exists().where(DBUser.name == auth_login_request.id)).scalar() > 0:
        return (ApiResponse(code="500", type="string", message="Already Exist"), 500)
    else:
        user = DBUser()
        user.name = auth_login_request.id
        salt = bcrypt.gensalt(rounds=10, prefix=b'2a')
        user.password = bcrypt.hashpw(bytes(auth_login_request.password, "utf-8"), salt).decode('utf8')
        user.jwt_secret = ""
        session.add(user)
        session.commit()
        return ApiResponse(code="200", type="string", message="OK")
