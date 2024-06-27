#!/usr/bin/env python3
"""Module for session management
"""

from api.v1.auth.auth import Auth
from uuid import uuid4
from typing import List, TypeVar


class SessionAuth(Auth):
    """Session management class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''self descriptive'''
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
