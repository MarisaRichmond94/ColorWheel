# pylint: disable=global-statement
from chalice import Chalice

APP = None

def create_chalice_app():
    global APP

    if APP is None:
        APP = Chalice(app_name="colorwheel")

    return APP
