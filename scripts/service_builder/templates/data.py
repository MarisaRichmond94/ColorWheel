from settings import (
    DATA_TYPE,
    METHODS,
    PLURAL_PARAM_TYPE,
    SCHEMA_NAME,
    SERVICE_NAME,
    SINGULAR_PARAM_TYPE,
    TABLE_TYPE,
)


def generate_data_imports() -> str:
    """Generates a base string for a basic data file.

    Returns:
        A string populated with the given service name.
    """
    add_imports = any(method in ['POST', 'GET_BY_ID', 'PATCH', 'DELETE_BY_ID'] for method in METHODS)

    data_imports = f'"""Data layer for the {SERVICE_NAME} service."""\n'
    data_imports += (
        (
            "from typing import Optional\n"
            "\n"
        )
        if add_imports else ''
    )
    data_imports += (
        f"from db_models.{TABLE_TYPE}_{SERVICE_NAME} import {TABLE_TYPE.capitalize()}{SCHEMA_NAME}\n"
        "from utils import db\n"
    )
    data_imports += "from utils.types import UUIDType\n" if add_imports else ''
    data_imports += (
        (
            f"from restful_services.{SERVICE_NAME}.model_layer.data_schemas import (\n"
            f"    {SCHEMA_NAME}Schema,\n"
            f"    Populated{SCHEMA_NAME}Schema,\n"
            f")\n"
            "\n"
        )
        if TABLE_TYPE == 'fct'
        else (
            f"from restful_services.{SERVICE_NAME}.model_layer.data_schemas import {SCHEMA_NAME}Schema\n"
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
        f'def create_{DATA_TYPE}(\n'
        "    # pass in variables\n"
        ') -> Optional[dict]:\n'
        f'    """Creates a new {SINGULAR_PARAM_TYPE} in the {TABLE_TYPE}_{SERVICE_NAME} table.\n'
        "\n"
        "    Args:\n"
        "        # list any given params here\n"
        "\n"
        "    Returns:\n"
        f'        A newly created {SINGULAR_PARAM_TYPE} else None.\n'
        '    """\n'
        "    with db.session_scope() as session:\n"
        f"        new_{DATA_TYPE} = {TABLE_TYPE.capitalize()}{SCHEMA_NAME}(\n"
        "            # pass in variables\n"
        "        )\n"
        "\n"
        f"        if new_{DATA_TYPE}:\n"
        f"            session.add(new_{DATA_TYPE})\n"
        "            session.commit()\n"
        f"            return {SCHEMA_NAME}Schema().dump(new_{DATA_TYPE})\n"
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
        f"def get_{SERVICE_NAME}() -> list:\n"
        f'    """Gets all {PLURAL_PARAM_TYPE} from the {TABLE_TYPE}_{SERVICE_NAME} table.\n'
        "\n"
        "    Returns:\n"
        f'        A list of {PLURAL_PARAM_TYPE}.\n'
        '    """\n'
        "    with db.session_scope() as session:\n"
        f"        {SERVICE_NAME} = session.query({TABLE_TYPE.capitalize()}{SCHEMA_NAME}).all()\n"
        f"        return {'Populated' if TABLE_TYPE == 'fct' else ''}{SCHEMA_NAME}Schema(many=True).dump({SERVICE_NAME}) if {SERVICE_NAME} else []\n"
        "\n"
    )


def generate_data_get_by_id_function() -> str:
    """Generates a basic GET by id function using established constants.

    Returns:
        A string representing a basic GET by id function.
    """
    return (
        "\n"
        f"def get_{DATA_TYPE}_by_id({DATA_TYPE}_id: UUIDType) -> Optional[dict]:\n"
        f'    """Gets a {SINGULAR_PARAM_TYPE} from the {TABLE_TYPE}_{SERVICE_NAME} table by the given id.\n'
        "\n"
        "    Args:\n"
        f'        {DATA_TYPE}_id - The primary key of a {SINGULAR_PARAM_TYPE} in the {TABLE_TYPE}_{SERVICE_NAME} table.\n'
        "\n"
        "    Returns:\n"
        f'        A {SINGULAR_PARAM_TYPE} with the given id else None.\n'
        '    """\n'
        "    with db.session_scope() as session:\n"
        f"        {DATA_TYPE} = session.query({TABLE_TYPE.capitalize()}{SCHEMA_NAME}).filter_by(id={DATA_TYPE}_id).one_or_none()\n"
        f"        return {'Populated' if TABLE_TYPE == 'fct' else ''}{SCHEMA_NAME}Schema().dump({DATA_TYPE}) if {DATA_TYPE} else None\n"
        "\n"
    )


def generate_data_update_function() -> str:
    """Generates a basic PATCH function using established constants.

    Returns:
        A string representing a basic PATCH function.
    """
    return (
        "\n"
        f'def update_{DATA_TYPE}(\n'
        f'    {DATA_TYPE}_id: UUIDType,\n'
        "    # pass any other given params\n"
        ') -> Optional[dict]:\n'
        f'    """Updates a {DATA_TYPE} in the {TABLE_TYPE}_{SERVICE_NAME} table by the given id.\n'
        "\n"
        "    Args:\n"
        f'        {DATA_TYPE}_id - The primary key of a {DATA_TYPE} in the {TABLE_TYPE}_{SERVICE_NAME} table.\n'
        "        # list any other given params here\n"
        "\n"
        "    Returns:\n"
        f'        An updated {DATA_TYPE} with the given id else None.\n'
        '    """\n'
        "    with db.session_scope() as session:\n"
        f"        {DATA_TYPE} = session.query({TABLE_TYPE.capitalize()}{SCHEMA_NAME}).filter_by(id={DATA_TYPE}_id).one_or_none()\n"
        "\n"
        f"        if {DATA_TYPE}:\n"
        "            # update entity\n"
        "            session.commit()\n"
        f"            return {SCHEMA_NAME}Schema().dump({DATA_TYPE})\n"
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
        f'def delete_{SERVICE_NAME}(\n'
        "    # pass any given params\n"
        ') -> list:\n'
        f'    """Deletes {PLURAL_PARAM_TYPE} from the {TABLE_TYPE}_{SERVICE_NAME} table using given params.\n'
        "\n"
        "    Args:\n"
        "        # list any given params here\n"
        "\n"
        "    Returns:\n"
        f'        A list of {PLURAL_PARAM_TYPE} deleted using given params.\n'
        '    """\n'
        "    with db.session_scope() as session:\n"
        f"        {SERVICE_NAME} = session.query({TABLE_TYPE.capitalize()}{SCHEMA_NAME}).filter_by().all()\n"
        "\n"
        f"        if {SERVICE_NAME}:\n"
        f"            for {DATA_TYPE} in {SERVICE_NAME}:\n"
        f"                session.delete({DATA_TYPE})\n"
        "                session.commit()\n"
        f"                return {SCHEMA_NAME}Schema(many=True).dump({SERVICE_NAME})\n"
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
        f"def delete_{DATA_TYPE}_by_id({DATA_TYPE}_id: UUIDType) -> Optional[dict]:\n"
        f'    """Deletes a {SINGULAR_PARAM_TYPE} from the {TABLE_TYPE}_{SERVICE_NAME} table by the given id.\n'
        "\n"
        "    Args:\n"
        f'        {DATA_TYPE}_id - The primary key of a {SINGULAR_PARAM_TYPE} in the {TABLE_TYPE}_{SERVICE_NAME} table.\n'
        "\n"
        "    Returns:\n"
        f'        A deleted {SINGULAR_PARAM_TYPE} with the given id else None.\n'
        '    """\n'
        "    with db.session_scope() as session:\n"
        f"        {DATA_TYPE} = session.query({TABLE_TYPE.capitalize()}{SCHEMA_NAME}).filter_by(id={DATA_TYPE}_id).one_or_none()\n"
        "\n"
        f"        if {DATA_TYPE}:\n"
        f"            session.delete({DATA_TYPE})\n"
        "            session.commit()\n"
        f"            return {SCHEMA_NAME}Schema().dump({DATA_TYPE})\n"
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
