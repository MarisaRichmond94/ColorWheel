import settings as args


def generate_data_imports() -> str:
    """Generates a base string for a basic data file.

    Returns:
        A string populated with the given service name.
    """
    methods = args.METHODS.split(' ')
    add_imports = any(
        method in ['POST', 'GET_BY_ID', 'PATCH', 'DELETE_BY_ID'] for method in methods
    )

    data_imports = f'"""Data layer for the {args.SERVICE_NAME} service."""\n'
    data_imports += (
        (
            "from typing import Optional\n"
            "\n"
        )
        if add_imports else ''
    )
    data_imports += (
        f"from db_models.{args.TABLE_TYPE}_{args.SERVICE_NAME} import "
        f"{args.TABLE_TYPE.capitalize()}{args.SCHEMA_NAME}\n"
        "from utils import db\n"
    )
    data_imports += "from utils.types import UUIDType\n" if add_imports else ''
    data_imports += (
        (
            f"from restful_services.{args.SERVICE_NAME}.model_layer.data_schemas import (\n"
            f"    {args.SCHEMA_NAME}Schema,\n"
            f"    Populated{args.SCHEMA_NAME}Schema,\n"
            f")\n"
            "\n"
        )
        if args.TABLE_TYPE == 'fct'
        else (
            f"from restful_services.{args.SERVICE_NAME}.model_layer.data_schemas import "
            f"{args.SCHEMA_NAME}Schema\n"
            "\n"
        )
    )
    return data_imports


def generate_data_function(method: str) -> str:
    """Generates an data function using the given method.

    Args:
        method - The base data method used to determine which function to generate (e.g. 'GET').

    Returns:
        A generated function associated with the given method else None.
    """
    data_generation_func = data_function_dict[method]
    if data_generation_func:
        return data_generation_func()
    print(f'No matching data function for given method: "{method}".')
    return None


def generate_data_create_function() -> str:
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
        '    """\n'
        "    with db.session_scope() as session:\n"
        f"        new_{args.DATA_TYPE} = {args.TABLE_TYPE.capitalize()}{args.SCHEMA_NAME}(\n"
        f'            id={args.DATA_TYPE}_id\n'
        "            # pass in variables\n"
        "        )\n"
        "\n"
        f"        if new_{args.DATA_TYPE}:\n"
        f"            session.add(new_{args.DATA_TYPE})\n"
        "            session.commit()\n"
        f"            return {args.SCHEMA_NAME}Schema().dump(new_{args.DATA_TYPE})\n"
        "        return None\n"
        "\n"
    )


def generate_data_get_function() -> str:
    """Generates a basic GET function using established constants.

    Returns:
        A string representing a basic GET function.
    """
    return (
        "\n"
        f"def get_{args.SERVICE_NAME}() -> list:\n"
        f'    """Gets all {args.PLURAL_PARAM_TYPE} from the {args.TABLE_TYPE}_{args.SERVICE_NAME} '
        'table.\n'
        "\n"
        "    Returns:\n"
        f'        A list of {args.PLURAL_PARAM_TYPE}.\n'
        '    """\n'
        "    with db.session_scope() as session:\n"
        f"        {args.SERVICE_NAME} = "
        f"session.query({args.TABLE_TYPE.capitalize()}{args.SCHEMA_NAME}).all()\n"
        f"        return {'Populated' if args.TABLE_TYPE == 'fct' else ''}{args.SCHEMA_NAME}"
        f"Schema(many=True).dump({args.SERVICE_NAME}) if {args.SERVICE_NAME} else []\n"
        "\n"
    )


def generate_data_get_by_id_function() -> str:
    """Generates a basic GET by id function using established constants.

    Returns:
        A string representing a basic GET by id function.
    """
    return (
        "\n"
        f"def get_{args.DATA_TYPE}_by_id({args.DATA_TYPE}_id: UUIDType) -> Optional[dict]:\n"
        f'    """Gets a {args.SINGULAR_PARAM_TYPE} from the {args.TABLE_TYPE}_{args.SERVICE_NAME} '
        f'table by the given id.\n'
        "\n"
        "    Args:\n"
        f'        {args.DATA_TYPE}_id - The primary key of a {args.SINGULAR_PARAM_TYPE} in the '
        f'{args.TABLE_TYPE}_{args.SERVICE_NAME} table.\n'
        "\n"
        "    Returns:\n"
        f'        A {args.SINGULAR_PARAM_TYPE} with the given id else None.\n'
        '    """\n'
        "    with db.session_scope() as session:\n"
        f"        {args.DATA_TYPE} = session.query({args.TABLE_TYPE.capitalize()}"
        f"{args.SCHEMA_NAME}).filter_by(id={args.DATA_TYPE}_id).one_or_none()\n"
        f"        return {'Populated' if args.TABLE_TYPE == 'fct' else ''}"
        f"{args.SCHEMA_NAME}Schema()."
        f"dump({args.DATA_TYPE}) if {args.DATA_TYPE} else None\n"
        "\n"
    )


def generate_data_update_function() -> str:
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
        f'    """Updates a {args.DATA_TYPE} in the {args.TABLE_TYPE}_{args.SERVICE_NAME} '
        'table by the given id.\n'
        "\n"
        "    Args:\n"
        f'        {args.DATA_TYPE}_id - The primary key of a {args.DATA_TYPE} in the '
        f'{args.TABLE_TYPE}_{args.SERVICE_NAME} table.\n'
        "        # list any other given params here\n"
        "\n"
        "    Returns:\n"
        f'        An updated {args.DATA_TYPE} with the given id else None.\n'
        '    """\n'
        "    with db.session_scope() as session:\n"
        f"        {args.DATA_TYPE} = session.query({args.TABLE_TYPE.capitalize()}"
        f"{args.SCHEMA_NAME}).filter_by(id={args.DATA_TYPE}_id).one_or_none()\n"
        "\n"
        f"        if {args.DATA_TYPE}:\n"
        "            # update entity\n"
        "            session.commit()\n"
        f"            return {args.SCHEMA_NAME}Schema().dump({args.DATA_TYPE})\n"
        "        return None\n"
        "\n"
    )


def generate_data_delete_function() -> str:
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
        "    with db.session_scope() as session:\n"
        f"        {args.SERVICE_NAME} = session.query({args.TABLE_TYPE.capitalize()}"
        f"{args.SCHEMA_NAME}).filter_by().all()\n"
        "\n"
        f"        if {args.SERVICE_NAME}:\n"
        f"            for {args.DATA_TYPE} in {args.SERVICE_NAME}:\n"
        f"                session.delete({args.DATA_TYPE})\n"
        "                session.commit()\n"
        f"                return {args.SCHEMA_NAME}Schema(many=True).dump({args.SERVICE_NAME})\n"
        "        return []\n"
        "\n"
    )


def generate_data_delete_by_id_function() -> str:
    """Generates a basic DELETE by id function using established constants.

    Returns:
        A string representing a basic DELETE by id function.
    """
    return (
        "\n"
        f"def delete_{args.DATA_TYPE}_by_id({args.DATA_TYPE}_id: UUIDType) -> Optional[dict]:\n"
        f'    """Deletes a {args.SINGULAR_PARAM_TYPE} from the {args.TABLE_TYPE}_'
        f'{args.SERVICE_NAME} table by the given id.\n'
        "\n"
        "    Args:\n"
        f'        {args.DATA_TYPE}_id - The primary key of a {args.SINGULAR_PARAM_TYPE} in the '
        f'{args.TABLE_TYPE}_{args.SERVICE_NAME} table.\n'
        "\n"
        "    Returns:\n"
        f'        A deleted {args.SINGULAR_PARAM_TYPE} with the given id else None.\n'
        '    """\n'
        "    with db.session_scope() as session:\n"
        f"        {args.DATA_TYPE} = session.query({args.TABLE_TYPE.capitalize()}"
        f"{args.SCHEMA_NAME}).filter_by(id={args.DATA_TYPE}_id).one_or_none()\n"
        "\n"
        f"        if {args.DATA_TYPE}:\n"
        f"            session.delete({args.DATA_TYPE})\n"
        "            session.commit()\n"
        f"            return {args.SCHEMA_NAME}Schema().dump({args.DATA_TYPE})\n"
        "        return None\n"
        "\n"
    )


data_function_dict = {
    'POST': generate_data_create_function,
    'GET': generate_data_get_function,
    'GET_BY_ID': generate_data_get_by_id_function,
    'PATCH': generate_data_update_function,
    'DELETE': generate_data_delete_function,
    'DELETE_BY_ID': generate_data_delete_by_id_function,
}
