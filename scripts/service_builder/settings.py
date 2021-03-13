import os

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
    """Set environment variables so that they will be accessible to templates.

    Args:
        arg_dict - A dictionary containing all necessary arguments.
    """
    os.environ['data_type'] = arg_dict.get('data_type', '')
    os.environ['methods'] = arg_dict.get('methods', '')
    os.environ['plural_param_type'] = arg_dict.get('plural_param_type', '')
    os.environ['schema_name'] = arg_dict.get('schema_name', '')
    os.environ['schema_type'] = arg_dict.get('schema_type', '')
    os.environ['service_name'] = arg_dict.get('service_name', '')
    os.environ['singular_param_type'] = arg_dict.get('singular_param_type', '')
    os.environ['table_type'] = arg_dict.get('table_type', '')
    os.environ['valid_api_schema_methods'] = arg_dict.get('valid_api_schema_methods', '')
