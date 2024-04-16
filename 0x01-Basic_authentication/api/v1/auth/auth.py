#!/usr/bin/env python3
""" Module of for authentication
"""

from flask import request
from typing import List, TypeVar


class Auth():
    """ Class that defines the Basic
        authentication methods
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require authentication to resources
        """
        if not path:
            return True
        if not excluded_paths or len(excluded_paths) == 0:
            return True

        for patha in excluded_paths:
            if path + '/' == patha:
                return False
            if path == patha:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ The authorization header
        """
        if request is None:
            return None
        if "Authorization" not in request.headers:
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """ The User to be authenticate upon request
        """
        return None
