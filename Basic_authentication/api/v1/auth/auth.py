from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Public method to determine if a given path requires authentication.

        Args:
        path (str): The path to check.
        excluded_paths (List[str]): A list of paths that are excluded
        from authentication.

        Returns:
        bool: False for now, as the logic will be implemented later.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
                Public method to get the authorization header from the request.

                Args:
                    request (Flask request object, optional):
                    The request object. Defaults to None.

                Returns:
                    str: None for now, as the logic will be implemented later.
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
