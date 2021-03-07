from settings import (
    PLURAL_PARAM_TYPE,
    SCHEMA_NAME,
    SCHEMA_TYPE,
    SERVICE_NAME,
    SINGULAR_PARAM_TYPE,
    VALID_API_SCHEMA_METHODS,
)


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
        A generated function associated with the given method else an empty string.
    """
    api_schema_generation_func = (
        api_schema_function_dict[method] if method in VALID_API_SCHEMA_METHODS else None
    )
    if api_schema_generation_func:
        return api_schema_generation_func()
    return ''


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
