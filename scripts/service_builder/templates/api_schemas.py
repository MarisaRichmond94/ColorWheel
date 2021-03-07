def set_api_schema_constants(arg_dict: dict) -> None:
    """Sets global constants needed to generate templates.

    Args:
        arg_dict: Dict containing constant values.
    """
    global PLURAL_PARAM_TYPE
    PLURAL_PARAM_TYPE = arg_dict.get('plural_param_type', '')
    global SCHEMA_NAME
    SCHEMA_NAME = arg_dict.get('schema_name', '')
    global SCHEMA_TYPE
    SCHEMA_TYPE = arg_dict.get('schema_type', '')
    global SINGULAR_PARAM_TYPE
    SINGULAR_PARAM_TYPE = arg_dict.get('singular_param_type', '')
    global SERVICE_NAME
    SERVICE_NAME = arg_dict.get('service_name', '')
    global VALID_API_SCHEMA_METHODS
    VALID_API_SCHEMA_METHODS = arg_dict.get('valid_api_schema_methods', '')


def generate_api_schema_imports() -> str:
    """Generates a base string for a basic api_schema file.

    Returns:
        A string populated with the given service name and schema import.
    """
    return (
        f'"""API schemas for the {SERVICE_NAME} service."""\n'
        "from marshmallow import fields, Schema\n"
        "\n"
    )


def generate_api_schema_function(method: str) -> str:
    """Generates an api_schema function using the given method.

    Args:
        method - The base api_schema method used to determine which function to generate (e.g. 'GET').

    Returns:
        A generated function associated with the given method else None.
    """
    api_schema_generation_func = (
        api_schema_function_dict[method] if method in VALID_API_SCHEMA_METHODS else None
    )
    if api_schema_generation_func:
        return api_schema_generation_func()
    print(f'No matching api_schema function for given method: "{method}".')
    return None


def generate_api_schema_create_function() -> str:
    """Generates a basic POST function using established constants.

    Returns:
        A string representing a basic POST function.
    """
    return (
        "\n"
        f"class Create{SCHEMA_TYPE}BodySchema(Schema):\n"
        f'    """Schema for creating a new {SINGULAR_PARAM_TYPE}."""\n'
        "    pass # TODO - set expected values\n"
        "\n"
    )


def generate_api_schema_get_function() -> str:
    """Generates a basic GET function using established constants.

    Returns:
        A string representing a basic GET function.
    """
    return (
        "\n"
        f"class Get{SCHEMA_NAME}QuerySchema(Schema):\n"
        f'    """Schema for getting {PLURAL_PARAM_TYPE}."""\n'
        "    pass # TODO - set expected values\n"
        "\n"
    )


def generate_api_schema_update_function() -> str:
    """Generates a basic PATCH function using established constants.

    Returns:
        A string representing a basic PATCH function.
    """
    return (
        "\n"
        f"class Update{SCHEMA_TYPE}BodySchema(Schema):\n"
        f'    """Schema for updating a {SINGULAR_PARAM_TYPE}."""\n'
        "    pass # TODO - set expected values\n"
        "\n"
    )


def generate_api_schema_delete_function() -> str:
    """Generates a basic DELETE function using established constants.

    Returns:
        A string representing a basic DELETE function.
    """
    return (
        "\n"
        f"class Delete{SCHEMA_NAME}QuerySchema(Schema):\n"
        f'    """Schema for deleting {PLURAL_PARAM_TYPE}."""\n'
        "    pass # TODO - set expected values\n"
        "\n"
    )


api_schema_function_dict = {
    'POST': generate_api_schema_create_function,
    'GET': generate_api_schema_get_function,
    'PATCH': generate_api_schema_update_function,
    'DELETE': generate_api_schema_delete_function,
}
