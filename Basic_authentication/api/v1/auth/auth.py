#!/usr/bin/env python3
""" Module of Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class to manage the API authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Public method to determine if a given path requires authentication.
        """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
            # Add slash to all cases for consistency
        if path[-1] != '/':
            path += '/'
        if excluded_paths[-1] != '/':
            excluded_paths += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Public method to get the authorization header from the request.

        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
               Public method to get the current user from the request.

               Args:
                   request (Flask request object, optional):
                   The request object. Defaults to None.

               Returns:
                   TypeVar('User'): None for now,
                   as the logic will be implemented later.
               """
        return None
