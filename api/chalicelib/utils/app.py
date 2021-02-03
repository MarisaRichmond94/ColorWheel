"""Functionality for creating the Chalice app and making it globally accessible"""
# pylint: disable=global-statement
from chalice import Chalice

APP = None

def create_chalice_app():
    """Creates a new globally accessible Chalice app if one does not already exist

    Returns:
        A chalice application object
    """
    global APP

    if APP is None:
        APP = Chalice(app_name="colorwheel")

    return APP
