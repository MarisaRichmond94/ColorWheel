"""Place to save all static variables related to aws"""
import os
import sys

from loguru import logger as log

# Environment Variables
try:
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_REGION = os.getenv("AWS_REGION", "us-west-2")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AUTHENTICATION_BUCKET_NAME = os.getenv(
        "AUTHENTICATION_BUCKET_NAME",
        "colorwheel_authentication"
    )
except KeyError as exp:
    log.error(f'Environment variable "{exp.args[0]}" is not set.')
    sys.exit(1)
