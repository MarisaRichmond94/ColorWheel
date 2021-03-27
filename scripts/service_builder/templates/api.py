import settings as args


def generate_api_imports() -> str:
    """Generates a base string for a basic api file.

    Returns:
        A string populated with the given service name and schema import.
    """
    methods = args.METHODS.split(' ')
    api_imports = f'"""API layer for the {args.SERVICE_NAME} service."""\n'
    api_imports += (
        ("from typing import Optional\n" '\n')
        if any(method in ['POST', 'GET_BY_ID', 'PATCH', 'DELETE_BY_ID'] for method in methods)
        else ''
    )
    api_imports += (
        "\n"
        "from chalice import Blueprint\n"
        "\n"
        f'from restful_services.{args.SERVICE_NAME}.business_layer import business\n'
    )
    schema_import = determine_schema_import()
    api_imports += (
        (
            f'from restful_services.{args.SERVICE_NAME}.model_layer.api_schemas import (\n'
            f'{schema_import}'
            ')\n'
        ) if schema_import else ''
    )
    api_imports += (
        "from utils.api_handler import api_handler\n"
        '\n'
        "api = Blueprint(__name__)\n"
        '\n'
    )
    return api_imports


def determine_schema_import() -> str:
    """Dynamically generates a schema import string based on methods requiring a schema.

    Returns:
        An import string based on required methods else an empty string.
    """
    api_schema_import_dict = {
        'POST': f"Create{args.SCHEMA_TYPE}BodySchema",
        'GET': f"Get{args.SCHEMA_NAME}QuerySchema",
        'PATCH': f"Update{args.SCHEMA_TYPE}BodySchema",
        'DELETE': f"Delete{args.SCHEMA_NAME}QuerySchema",
    }
    schema_import = ''
    methods = args.METHODS.split(' ')
    valid_api_schema_methods = args.VALID_API_SCHEMA_METHODS.split(' ')
    for method in methods:
        if method in valid_api_schema_methods:
            schema_import += (f"    {api_schema_import_dict[method]},\n")
    return schema_import


def generate_api_function(method: str) -> str:
    """Generates an api function using the given method.

    Args:
        method - The base api method used to determine which function to generate (e.g. 'GET').

    Returns:
        A generated function associated with the given method else None.
    """
    api_generation_func = api_function_dict[method]
    if api_generation_func:
        return api_generation_func()
    print(f'No matching api function for given method: "{method}".')
    return None


def generate_api_create_function() -> str:
    """Generates a basic POST function using established constants.

    Returns:
        A string representing a basic POST function.
    """
    return (
        '\n'
        '@api_handler(\n'
        '    api=api,\n'
        f'    path="/{args.SERVICE_NAME.replace("_", "-")}",\n'
        '    methods=["POST"],\n'
        f'    body_schema=Create{args.SCHEMA_TYPE}BodySchema,\n'
        ")\n"
        f'def create_{args.DATA_TYPE}() -> Optional[dict]:\n'
        f'    """Creates a new {args.SINGULAR_PARAM_TYPE} in the '
        f'{args.TABLE_TYPE}_{args.SERVICE_NAME} table.\n'
        "\n"
        "    Returns:\n"
        f'        A newly created {args.SINGULAR_PARAM_TYPE} else None.\n'
        '    """\n'
        f'    return business.create_{args.DATA_TYPE}(\n'
        '        # pass in variables\n'
        f'        {args.DATA_TYPE}_id=api.handled_request.body.get(id)\n'
        '    )\n'
        '\n'
    )


def generate_api_get_function() -> str:
    """Generates a basic GET function using established constants.

    Returns:
        A string representing a basic GET function.
    """
    return (
        '\n'
        '@api_handler(\n'
        '    api=api,\n'
        f'    path="/{args.SERVICE_NAME.replace("_", "-")}",\n'
        '    methods=["GET"],\n'
        f'    query_schema=Get{args.SCHEMA_NAME}QuerySchema,\n'
        ")\n"
        f'def get_{args.SERVICE_NAME}() -> list:\n'
        f'    """Gets {args.PLURAL_PARAM_TYPE} from the {args.TABLE_TYPE}_{args.SERVICE_NAME} '
        f'table filtered by given params.\n'
        "\n"
        "    Returns:\n"
        f'        A list of {args.PLURAL_PARAM_TYPE} filtered by any given params.\n'
        '    """\n'
        f'    return business.get_{args.SERVICE_NAME}(\n'
        '        # pass in variables\n'
        '    )\n'
        '\n'
    )


def generate_api_get_by_id_function() -> str:
    """Generates a basic GET by id function using established constants.

    Returns:
        A string representing a basic GET by id function.
    """
    return (
        '\n'
        '@api_handler(\n'
        '    api=api,\n'
        f'    path="/{args.SERVICE_NAME.replace("_", "-")}/{{{args.DATA_TYPE}_id}}",\n'
        '    methods=["GET"],\n'
        ")\n"
        f'def get_{args.DATA_TYPE}_by_id({args.DATA_TYPE}_id: str) -> Optional[dict]:\n'
        f'    """Gets a {args.SINGULAR_PARAM_TYPE} from the {args.TABLE_TYPE}_{args.SERVICE_NAME} '
        'table by the given id.\n'
        "\n"
        "    Args:\n"
        f'        {args.DATA_TYPE}_id - The primary key of a {args.SINGULAR_PARAM_TYPE} in the '
        f'{args.TABLE_TYPE}_{args.SERVICE_NAME} table.\n'
        "\n"
        "    Returns:\n"
        f'        A {args.SINGULAR_PARAM_TYPE} with the given id else None.\n'
        '    """\n'
        f'    return business.get_{args.DATA_TYPE}_by_id({args.DATA_TYPE}_id={args.DATA_TYPE}_id)\n'
        '\n'
    )


def generate_api_update_function() -> str:
    """Generates a basic PATCH function using established constants.

    Returns:
        A string representing a basic PATCH function.
    """
    return (
        '\n'
        '@api_handler(\n'
        '    api=api,\n'
        f'    path="/{args.SERVICE_NAME.replace("_", "-")}/{{{args.DATA_TYPE}_id}}",\n'
        '    methods=["PATCH"],\n'
        f'    body_schema=Update{args.SCHEMA_TYPE}BodySchema,\n'
        ")\n"
        f'def update_{args.DATA_TYPE}({args.DATA_TYPE}_id: str) -> Optional[dict]:\n'
        f'    """Updates a {args.SINGULAR_PARAM_TYPE} in the {args.TABLE_TYPE}_{args.SERVICE_NAME} '
        'table by the given id.\n'
        "\n"
        "    Args:\n"
        f'        {args.DATA_TYPE}_id - The primary key of a {args.SINGULAR_PARAM_TYPE} in the '
        f'{args.TABLE_TYPE}_{args.SERVICE_NAME} table.\n'
        "\n"
        "    Returns:\n"
        f'        An updated {args.SINGULAR_PARAM_TYPE} with the given id else None.\n'
        '    """\n'
        f'    return business.update_{args.DATA_TYPE}(\n'
        f'        {args.DATA_TYPE}_id={args.DATA_TYPE}_id,\n'
        '        # pass in variables\n'
        '    )\n'
        '\n'
    )


def generate_api_delete_function() -> str:
    """Generates a basic DELETE function using established constants.

    Returns:
        A string representing a basic DELETE function.
    """
    return (
        '\n'
        '@api_handler(\n'
        '    api=api,\n'
        f'    path="/{args.SERVICE_NAME.replace("_", "-")}",\n'
        '    methods=["DELETE"],\n'
        f'    query_schema=Delete{args.SCHEMA_NAME}QuerySchema,\n'
        ")\n"
        f'def delete_{args.SERVICE_NAME}() -> list:\n'
        f'    """Deletes {args.PLURAL_PARAM_TYPE} from the {args.TABLE_TYPE}_{args.SERVICE_NAME} '
        'table using given params.\n'
        "\n"
        "    Returns:\n"
        f'        A list of {args.PLURAL_PARAM_TYPE} deleted using given params.\n'
        '    """\n'
        f'    return business.delete_{args.SERVICE_NAME}(\n'
        '        # pass in variables\n'
        '    )\n'
        '\n'
    )


def generate_api_delete_by_id_function() -> str:
    """Generates a basic DELETE by id function using established constants.

    Returns:
        A string representing a basic DELETE by id function.
    """
    return (
        '\n'
        '@api_handler(\n'
        '    api=api,\n'
        f'    path="/{args.SERVICE_NAME.replace("_", "-")}/{{{args.DATA_TYPE}_id}}",\n'
        '    methods=["DELETE"],\n'
        ")\n"
        f'def delete_{args.DATA_TYPE}_by_id({args.DATA_TYPE}_id: str) -> Optional[dict]:\n'
        f'    """Deletes a {args.SINGULAR_PARAM_TYPE} from the '
        f'{args.TABLE_TYPE}_{args.SERVICE_NAME} table by the given id.\n'
        "\n"
        "    Args:\n"
        f'        {args.DATA_TYPE}_id - The primary key of a {args.SINGULAR_PARAM_TYPE} in the '
        f'{args.TABLE_TYPE}_{args.SERVICE_NAME} table.\n'
        "\n"
        "    Returns:\n"
        f'        A deleted {args.SINGULAR_PARAM_TYPE} with the given id else None.\n'
        '    """\n'
        f'    return business.delete_'
        f'{args.DATA_TYPE}_by_id({args.DATA_TYPE}_id={args.DATA_TYPE}_id)\n'
        '\n'
    )


api_function_dict = {
    'POST': generate_api_create_function,
    'GET': generate_api_get_function,
    'GET_BY_ID': generate_api_get_by_id_function,
    'PATCH': generate_api_update_function,
    'DELETE': generate_api_delete_function,
    'DELETE_BY_ID': generate_api_delete_by_id_function,
}
