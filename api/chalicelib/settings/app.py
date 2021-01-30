"""Place to save all static variables related to the app"""
import os
import sys

from loguru import logger as log

# Environment Variables
try:
    AUTHORIZER_ARN = os.getenv('AUTHORIZER_ARN')
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_REGION = os.getenv('AWS_REGION', 'us-west-2')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    CORS_WHITELIST = os.getenv(
        'CORS_WHITELIST',
        'http://localhost http://localhost:3000'
    )
    DOMAIN = os.getenv('DOMAIN', 'http://localhost')
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'local')
except KeyError as exp:
    log.error(f'Environment variable "{exp.args[0]}" is not set.')
    sys.exit(1)

if (ENVIRONMENT in ['local'] and not (AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY)):
    log.warning(
        'One or both variables ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY"] are not set.'
    )
