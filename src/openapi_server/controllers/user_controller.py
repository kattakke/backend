import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.auth_login_request import AuthLoginRequest  # noqa: E501
from openapi_server.models.book import Book  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server import util
from db.models import Session, DBUser, DBBook, DBShelf
import bcrypt
from sqlalchemy.sql import exists
from sqlalchemy.sql import or_
from openapi_server.controllers.book_controller import get_book_info

def delete_user_info(authorization = None, user_id = None, token_info = None):  # noqa: E501
    """delete user info

    delete user info # noqa: E501

    :param authorization: bearer token
    :type authorization: str
    :param user_id: ID of user
    :type user_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    session = Session()
    if token_info["permission"] == "Admin" or user_id == token_info["id"]:
        if session.query(exists().where(DBUser.userId == user_id)).scalar() > 0:
            user = session.query(DBUser).filter(DBUser.userId == user_id).first()
            session.delete(user)
            session.commit()
            return None, 200
        else:
            return None, 404



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
        return None, 404
    


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
    session = Session()
    if session.query(exists().where(DBUser.userId == user_id)).scalar() > 0:
        user = session.query(DBUser).filter(DBUser.userId == user_id).first()
        shelf = user.shelf

        if (not title is None) and not title == "":
            books = session.query(DBShelf, DBBook).filter(DBShelf.shelfId == shelf, DBShelf.book == DBBook.bookId, DBBook.title.contains(title))
        elif (not isbn is None) and not isbn == "":
            books = session.query(DBShelf, DBBook).filter(DBShelf.shelfId == shelf, DBShelf.book == DBBook.bookId, DBBook.isbn.contains(isbn))
        else:
            books = session.query(DBShelf, DBBook).filter(DBShelf.shelfId == shelf, DBShelf.book == DBBook.bookId)
        l = []
        for _, i in books.all():
            b = Book(book_id= str(i.bookId), isbn= i.isbn, title = i.title, author= i.author, image_path = i.imagePath, updated_at=i.updated_at, created_at=i.created_at)
            if not b is None:
                l.append(b)
        return l
    else:
        return None, 404


def patch_user_info(authorization = None, user_id = None, auth_login_request=None, token_info=None):  # noqa: E501
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
    
    session = Session()
    if token_info["permission"] == "Admin" or user_id == token_info["id"]:
        if session.query(exists().where(DBUser.userId == user_id)).scalar() > 0:
            user = session.query(DBUser).filter(DBUser.userId == user_id).first()
            user.name = auth_login_request.id
            user.password = auth_login_request.password
            session.commit()
            return None
        else:
            return (None, 404)

def user_register(auth_login_request=None):  # noqa: E501
    """register user

    register user # noqa: E501

    :param auth_login_request: 
    :type auth_login_request: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        auth_login_request = AuthLoginRequest.from_dict(connexion.request.get_json())  # noqa: E501
    session = Session()
    if session.query(exists().where(DBUser.name == auth_login_request.id)).scalar() > 0:
        return None, 500
    else:
        user = DBUser()
        user.name = auth_login_request.id
        salt = bcrypt.gensalt(rounds=10, prefix=b'2a')
        user.password = bcrypt.hashpw(bytes(auth_login_request.password, "utf-8"), salt).decode('utf8')
        user.jwt_secret = ""
        session.add(user)
        session.commit()
        return None
