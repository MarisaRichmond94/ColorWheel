import os
import sys

from loguru import logger as log


DATA_TYPE = os.getenv("data_type", "")
METHODS = os.getenv("methods", "")
PLURAL_PARAM_TYPE = os.getenv("plural_param_type", "")
SCHEMA_NAME = os.getenv("schema_name", "")
SCHEMA_TYPE = os.getenv("schema_type", "")
SERVICE_NAME = os.getenv("service_name", "")
SINGULAR_PARAM_TYPE = os.getenv("singular_param_type", "")
TABLE_TYPE = os.getenv("table_type", "")
VALID_API_SCHEMA_METHODS = os.getenv("valid_api_schema_methods", "")


def set_settings_variables(arg_dict: dict) -> None:
    DATA_TYPE = arg_dict.get('data_type', '')
    METHODS = arg_dict.get('methods', '')
    PLURAL_PARAM_TYPE = arg_dict.get('plural_param_type', '')
    SCHEMA_NAME = arg_dict.get('schema_name', '')
    SCHEMA_TYPE = arg_dict.get('schema_type', '')
    SERVICE_NAME = arg_dict.get('service_name', '')
    SINGULAR_PARAM_TYPE = arg_dict.get('singular_param_type', '')
    TABLE_TYPE = arg_dict.get('table_type', '')
    VALID_API_SCHEMA_METHODS = arg_dict.get('valid_api_schema_methods', '')
