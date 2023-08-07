# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Book(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, book_id=None, isbn=None, title=None, author=None, created_at=None, updated_at=None, image_path=None):  # noqa: E501
        """Book - a model defined in OpenAPI

        :param book_id: The book_id of this Book.  # noqa: E501
        :type book_id: str
        :param isbn: The isbn of this Book.  # noqa: E501
        :type isbn: str
        :param title: The title of this Book.  # noqa: E501
        :type title: str
        :param author: The author of this Book.  # noqa: E501
        :type author: str
        :param created_at: The created_at of this Book.  # noqa: E501
        :type created_at: datetime
        :param updated_at: The updated_at of this Book.  # noqa: E501
        :type updated_at: datetime
        :param image_path: The image_path of this Book.  # noqa: E501
        :type image_path: str
        """
        self.openapi_types = {
            'book_id': str,
            'isbn': str,
            'title': str,
            'author': str,
            'created_at': datetime,
            'updated_at': datetime,
            'image_path': str
        }

        self.attribute_map = {
            'book_id': 'bookId',
            'isbn': 'isbn',
            'title': 'title',
            'author': 'author',
            'created_at': 'createdAt',
            'updated_at': 'updatedAt',
            'image_path': 'imagePath'
        }

        self._book_id = book_id
        self._isbn = isbn
        self._title = title
        self._author = author
        self._created_at = created_at
        self._updated_at = updated_at
        self._image_path = image_path

    @classmethod
    def from_dict(cls, dikt) -> 'Book':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Book of this Book.  # noqa: E501
        :rtype: Book
        """
        return util.deserialize_model(dikt, cls)

    @property
    def book_id(self):
        """Gets the book_id of this Book.


        :return: The book_id of this Book.
        :rtype: str
        """
        return self._book_id

    @book_id.setter
    def book_id(self, book_id):
        """Sets the book_id of this Book.


        :param book_id: The book_id of this Book.
        :type book_id: str
        """

        self._book_id = book_id

    @property
    def isbn(self):
        """Gets the isbn of this Book.


        :return: The isbn of this Book.
        :rtype: str
        """
        return self._isbn

    @isbn.setter
    def isbn(self, isbn):
        """Sets the isbn of this Book.


        :param isbn: The isbn of this Book.
        :type isbn: str
        """

        self._isbn = isbn

    @property
    def title(self):
        """Gets the title of this Book.


        :return: The title of this Book.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Book.


        :param title: The title of this Book.
        :type title: str
        """

        self._title = title

    @property
    def author(self):
        """Gets the author of this Book.


        :return: The author of this Book.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this Book.


        :param author: The author of this Book.
        :type author: str
        """

        self._author = author

    @property
    def created_at(self):
        """Gets the created_at of this Book.


        :return: The created_at of this Book.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Book.


        :param created_at: The created_at of this Book.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Book.


        :return: The updated_at of this Book.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Book.


        :param updated_at: The updated_at of this Book.
        :type updated_at: datetime
        """

        self._updated_at = updated_at

    @property
    def image_path(self):
        """Gets the image_path of this Book.


        :return: The image_path of this Book.
        :rtype: str
        """
        return self._image_path

    @image_path.setter
    def image_path(self, image_path):
        """Sets the image_path of this Book.


        :param image_path: The image_path of this Book.
        :type image_path: str
        """

        self._image_path = image_path
