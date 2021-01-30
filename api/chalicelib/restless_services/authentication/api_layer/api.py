"""API layer for the endpoints of the authentication service"""
from chalice import Blueprint
from loguru import logger as log

api = Blueprint(__name__)


@api.route(
  '/authentication',
  methods=['POST'],
  api_key_required=False,
  authorizer=None,
)
def authenticate_user():
    """Authenticates a user against the user service

    Returns:
        AccessToken if the user is authenticated
    """
    log.debug('Ive been hit!')
