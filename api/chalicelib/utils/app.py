"""Reusable functionality for the app."""
# pylint: disable=global-statement
from chalice import Chalice

APP = None

def create_chalice_app():
    """Creates a global instance of the chalice app if one does not already exist."""
    global APP

    if APP is None:
        APP = Chalice(app_name="colorwheel")

    return APP
