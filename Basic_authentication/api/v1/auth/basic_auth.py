#!/usr/bin/env python3
""" Module of Basic Authentication
"""
from api.v1.auth.auth import Auth


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
