import settings as args


def generate_business_imports() -> str:
    """Generates a base string for a basic business file.

    Returns:
        A string populated with the given service name.
    """
    methods = args.METHODS.split(' ')
    add_imports = any(
        method in ['POST', 'GET_BY_ID', 'PATCH', 'DELETE_BY_ID'] for method in methods
    )

    business_imports = f'"""Business layer for the {args.SERVICE_NAME} service."""\n'
    business_imports += (
        (
            "from typing import Optional\n"
            "\n"
            "from utils.types import UUIDType\n"
            "from utils.validation import validate_params\n"
        )
        if add_imports else ''
    )
    business_imports += (
        f'from restful_services.{args.SERVICE_NAME}.data_layer import data\n'
        "\n"
    )
    return business_imports


def generate_business_function(method: str) -> str:
    """Generates an business function using the given method.

    Args:
        method - The base business method used to determine which function to generate (e.g. 'GET').

    Returns:
        A generated function associated with the given method else None.
    """
    business_generation_func = business_function_dict[method]
    if business_generation_func:
        return business_generation_func()
    print(f'No matching business function for given method: "{method}".')
    return None


def generate_business_create_function() -> str:
    """Generates a basic POST function using established constants.

    Returns:
        A string representing a basic POST function.
    """
    return (
        "\n"
        f'def create_{args.DATA_TYPE}(\n'
        "    # pass in variables\n"
        f'    {args.DATA_TYPE}_id: Optional[UUIDType]\n'
        ') -> Optional[dict]:\n'
        f'    """Creates a new {args.SINGULAR_PARAM_TYPE} in the '
        f'{args.TABLE_TYPE}_{args.SERVICE_NAME} table.\n'
        "\n"
        "    Args:\n"
        "        # list any given params here\n"
        f'        {args.DATA_TYPE}_id - The primary key to assign the {args.SINGULAR_PARAM_TYPE}\n'
        "\n"
        "    Returns:\n"
        f'        A newly created {args.SINGULAR_PARAM_TYPE} else None.\n'
        "\n"
        "    Raises:\n"
        "        InvalidParamException - If any of the given params are None.\n"
        '    """\n'
        "    validate_params(\n"
        f"        func='create_{args.DATA_TYPE}',\n"
        "        params={\n"
        "            # pass required params here\n"
        "        },\n"
        "    )\n"
        f"    return data.create_{args.DATA_TYPE}(\n"
        "        # pass in variables\n"
        f'        {args.DATA_TYPE}_id={args.DATA_TYPE}_id\n'
        "    )\n"
        "\n"
    )


def generate_business_get_function() -> str:
    """Generates a basic GET function using established constants.

    Returns:
        A string representing a basic GET function.
    """
    return (
        "\n"
        f'def get_{args.SERVICE_NAME}(\n'
        "    # pass in variables\n"
        ') -> list:\n'
        f'    """Gets {args.PLURAL_PARAM_TYPE} from the {args.TABLE_TYPE}_{args.SERVICE_NAME} '
        'table filtered by given params.\n'
        "\n"
        "    Args:\n"
        "        # list any given params here\n"
        "\n"
        "    Returns:\n"
        f'        A list of {args.PLURAL_PARAM_TYPE} filtered by any given params.\n'
        '    """\n'
        f"    return data.get_{args.SERVICE_NAME}()\n"
        "\n"
    )


def generate_business_get_by_id_function() -> str:
    """Generates a basic GET by id function using established constants.

    Returns:
        A string representing a basic GET by id function.
    """
    return (
        "\n"
        f'def get_{args.DATA_TYPE}_by_id({args.DATA_TYPE}_id: UUIDType) -> Optional[dict]:\n'
        f'    """Gets a {args.SINGULAR_PARAM_TYPE} from the {args.TABLE_TYPE}_{args.SERVICE_NAME} '
        'table by the given id.\n'
        "\n"
        "    Args:\n"
        f'        {args.DATA_TYPE}_id - The primary key of a {args.SINGULAR_PARAM_TYPE} in the '
        f'{args.TABLE_TYPE}_{args.SERVICE_NAME} table.\n'
        "\n"
        "    Returns:\n"
        f'        A {args.SINGULAR_PARAM_TYPE} with the given id else None.\n'
        "\n"
        "    Raises:\n"
        f"        InvalidParamException - If the given {args.DATA_TYPE}_id is None.\n"
        '    """\n'
        "    validate_params(\n"
        f"        func='get_{args.DATA_TYPE}_by_id',\n"
        f"        params={{'{args.DATA_TYPE}_id': {args.DATA_TYPE}_id}},\n"
        "    )\n"
        f"    return data.get_{args.DATA_TYPE}_by_id({args.DATA_TYPE}_id={args.DATA_TYPE}_id)\n"
        "\n"
    )


def generate_business_update_function() -> str:
    """Generates a basic PATCH function using established constants.

    Returns:
        A string representing a basic PATCH function.
    """
    return (
        "\n"
        f'def update_{args.DATA_TYPE}(\n'
        f'    {args.DATA_TYPE}_id: UUIDType,\n'
        "    # pass any other given params\n"
        ') -> Optional[dict]:\n'
        f'    """Updates a {args.SINGULAR_PARAM_TYPE} in the {args.TABLE_TYPE}_{args.SERVICE_NAME} '
        'table by the given id.\n'
        "\n"
        "    Args:\n"
        f'        {args.DATA_TYPE}_id - The primary key of a {args.SINGULAR_PARAM_TYPE} in the '
        f'{args.TABLE_TYPE}_{args.SERVICE_NAME} table.\n'
        "        # list any other given params here\n"
        "\n"
        "    Returns:\n"
        f'        An updated {args.SINGULAR_PARAM_TYPE} with the given id else None.\n'
        "\n"
        "    Raises:\n"
        f"        InvalidParamException - If any of the given params or the {args.DATA_TYPE}_id "
        "is None.\n"
        '    """\n'
        "    validate_params(\n"
        f"        func='update_{args.DATA_TYPE}',\n"
        f"        params={{\n"
        f"            '{args.DATA_TYPE}_id': {args.DATA_TYPE}_id,\n"
        "            # pass other required params here\n"
        "        }\n"
        "    )\n"
        f"    return data.update_{args.DATA_TYPE}(\n"
        f"        {args.DATA_TYPE}_id={args.DATA_TYPE}_id,\n"
        "        # pass any other given params\n"
        "    )\n"
        "\n"
    )


def generate_business_delete_function() -> str:
    """Generates a basic DELETE function using established constants.

    Returns:
        A string representing a basic DELETE function.
    """
    return (
        "\n"
        f'def delete_{args.SERVICE_NAME}(\n'
        "    # pass any given params\n"
        ') -> list:\n'
        f'    """Deletes {args.PLURAL_PARAM_TYPE} from the {args.TABLE_TYPE}_{args.SERVICE_NAME} '
        'table using given params.\n'
        "\n"
        "    Args:\n"
        "        # list any given params here\n"
        "\n"
        "    Returns:\n"
        f'        A list of {args.PLURAL_PARAM_TYPE} deleted using given params.\n'
        '    """\n'
        f"    return data.delete_{args.SERVICE_NAME}(\n"
        "        # pass any other given params\n"
        "    )\n"
        "\n"
    )


def generate_business_delete_by_id_function() -> str:
    """Generates a basic DELETE by id function using established constants.

    Returns:
        A string representing a basic DELETE by id function.
    """
    return (
        "\n"
        f'def delete_{args.DATA_TYPE}_by_id({args.DATA_TYPE}_id: UUIDType) -> Optional[dict]:\n'
        f'    """Deletes a {args.SINGULAR_PARAM_TYPE} from the '
        f'{args.TABLE_TYPE}_{args.SERVICE_NAME} table by the given id.\n'
        "\n"
        "    Args:\n"
        f'        {args.DATA_TYPE}_id - The primary key of a {args.SINGULAR_PARAM_TYPE} in the '
        f'{args.TABLE_TYPE}_{args.SERVICE_NAME} table.\n'
        "\n"
        "    Returns:\n"
        f'        A deleted {args.SINGULAR_PARAM_TYPE} with the given id else None.\n'
        "\n"
        "    Raises:\n"
        f"        InvalidParamException - If the given {args.DATA_TYPE}_id is None.\n"
        '    """\n'
        "    validate_params(\n"
        f"        func='delete_{args.DATA_TYPE}_by_id',\n"
        f"        params={{'{args.DATA_TYPE}_id': {args.DATA_TYPE}_id}},\n"
        "    )\n"
        f"    return data.delete_{args.DATA_TYPE}_by_id({args.DATA_TYPE}_id={args.DATA_TYPE}_id)\n"
        "\n"
    )


business_function_dict = {
    'POST': generate_business_create_function,
    'GET': generate_business_get_function,
    'GET_BY_ID': generate_business_get_by_id_function,
    'PATCH': generate_business_update_function,
    'DELETE': generate_business_delete_function,
    'DELETE_BY_ID': generate_business_delete_by_id_function,
}
