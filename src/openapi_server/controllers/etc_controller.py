import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server import util


def health_check():  # noqa: E501
    """Health Check API

    Always return 200 # noqa: E501


    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'
