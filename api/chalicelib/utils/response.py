"""Chalice response functionality."""
# pylint: disable=too-many-arguments,super-init-not-called
import json
from typing import Dict
import six

from chalice import Response as ChaliceResponse
from loguru import logger as log

from settings import app as app_settings


class Response(ChaliceResponse):
    """Builds a Chalice response from the given info."""
    def __init__(
        self,
        data: Dict = None,
        headers: Dict = None,
        message: str = 'success',
        origin: str = '',
        status_code: int = 200,
    ) -> None:
        self.body = dict(status_code=status_code, message=message)
        if data is not None:
            self.body['data'] = data
        self.headers = headers or {}
        if origin:
            self.origin = origin.lower()
            whitelist = app_settings.CORS_WHITELIST.lower()
            if self.origin in whitelist:
                self.headers['Access-Control-Allow-Origin'] = self.origin
            else:
                log.info(f'WARNING: Origin not found in  CORS whitelist: "{self.origin}"')
        else:
            log.info(f'WARNING: No Origin provided: "{origin}"')
        self.status_code = 200
        if not isinstance(self.body, six.string_types):
            self.body = json.dumps(self.body)

    def __str__(self) -> str:
        return (
            f'Response(headers={self.headers}, status_code="{self.status_code}", body={self.body})'
        )
