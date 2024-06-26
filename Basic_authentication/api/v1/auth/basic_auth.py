#!/usr/bin/env python3
""" Module of Basic Authentication
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ Basic Authentication Class """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Extract Base 64 Authorization Header """
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None
        elif authorization_header.split(" ")[0] != "Basic":
            return None
        else:
            return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Decodes the value of a base64 string """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_value = base64.b64decode(base64_authorization_header)
            if decoded_value:
                return decoded_value.decode('utf-8')
            else:
                raise BaseException()
        except BaseException:
            return None
