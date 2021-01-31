"""Place to save all static variables related to the app"""
import os
import sys

from loguru import logger as log

# Environment Variables
try:
    CORS_WHITELIST = os.getenv(
        "CORS_WHITELIST", "http://localhost http://localhost:3000"
    )
    DOMAIN = os.getenv("DOMAIN", "http://localhost")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "local")
except KeyError as exp:
    log.error(f'Environment variable "{exp.args[0]}" is not set.')
    sys.exit(1)
