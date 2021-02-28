#!/usr/bin/python
import os
import sys


### Helper Functions ###
def convert_snake_to_camel(snake_string: str) -> str:
    """Converts a string from being snake case to camel case.

    Args:
        snake_string: A snake cased string.

    Returns:
        A camel cased string.
    """
    split_snake_string = snake_string.split('_')
    capitalized_words_list = [item.capitalize() for item in split_snake_string]
    return ''.join(capitalized_words_list)


### Constants ###
SERVICE_NAME = sys.argv[1]
DATA_TYPE = sys.argv[2]
TABLE_TYPE = sys.argv[3]
CAMEL_CASE_SERVICE_NAME = convert_snake_to_camel(SERVICE_NAME)
PLAIN_SERVICE_NAME = ' '.join(SERVICE_NAME.split('_'))
CAMEL_CASE_DATA_TYPE = convert_snake_to_camel(DATA_TYPE)
PLAIN_DATA_TYPE = ' '.join(DATA_TYPE.split('_'))

ENDPOINTS = sys.argv[4:len(sys.argv)]
VALID_SCHEMA_ENDPOINTS = ['POST', 'GET', 'PATCH', 'DELETE']
API_SCHEMA_IMPORT_DICT = {
    'POST': f"Create{CAMEL_CASE_DATA_TYPE}BodySchema",
    'GET': f"Get{CAMEL_CASE_SERVICE_NAME}QuerySchema",
    'PATCH': f"Update{CAMEL_CASE_DATA_TYPE}BodySchema",
    'DELETE': f"Delete{CAMEL_CASE_SERVICE_NAME}QuerySchema",
}
SCHEMA_IMPORT_STRING = ''
for endpoint in ENDPOINTS:
        if endpoint in VALID_SCHEMA_ENDPOINTS:
            SCHEMA_IMPORT_STRING += (f"    {API_SCHEMA_IMPORT_DICT[endpoint]},\n")


### Main Functions ###
def main() -> None:
    """Generates a new service package using given sys.argv inputs."""
    navigate_to_restful_services()
    create_folders_and_inits()
    generate_api_layer()
    generate_business_layer()
    generate_data_layer()
    generate_model_layer()


def navigate_to_restful_services() -> None:
    """Navigates to the restful_services folder."""
    current_working_directory = os.getcwd().split('/')[-1]
    if current_working_directory != 'api' and current_working_directory != 'restful_services':
        print("Please run from the api folder or the restful_services folder.")
        sys.exit()

    if current_working_directory == 'api':
        print("Changing directories to restful_services...")
        os.chdir('./chalicelib/restful_services')


def create_folders_and_inits() -> None:
    """Creates all of the base-level folders needed for the new service given a valid name."""
    if not SERVICE_NAME:
        print('Missing required parameter "service name".')
        sys.exit()

    print(f'Generating new service with name ${SERVICE_NAME}...')
    os.mkdir(f'./{SERVICE_NAME}')
    os.chdir(f'./{SERVICE_NAME}')
    generate_init_file()
    os.mkdir(f'./api_layer')
    os.mkdir(f'./business_layer')
    os.mkdir(f'./data_layer')
    os.mkdir(f'./model_layer')


def generate_init_file() -> None:
    """Creates a blank __init__.py file."""
    with open(os.path.join(os.getcwd(), '__init__.py'), 'w') as init:
        pass


def generate_api_layer() -> None:
    """Generates the api layer files needed for the new service."""
    print(f'Generating api layer...')
    os.chdir('./api_layer')
    generate_init_file()

    with open(os.path.join(os.getcwd(), 'api.py'), 'w') as f:
        f.write(BASE_API_STRING)
        for endpoint in ENDPOINTS:
            f.write(API_DICT[endpoint])
    os.chdir('..')


def generate_business_layer() -> None:
    """Generates the business layer files needed for the new service."""
    print(f'Generating business layer...')
    os.chdir('./business_layer')
    generate_init_file()
    with open(os.path.join(os.getcwd(), 'business.py'), 'w') as f:
        f.write(BASE_BUSINESS_STRING)
        for endpoint in ENDPOINTS:
            f.write(BUSINESS_DICT[endpoint])
    os.chdir('..')


def generate_data_layer() -> None:
    """Generates the data layer files needed for the new service."""
    print(f'Generating data layer...')
    os.chdir('./data_layer')
    generate_init_file()
    with open(os.path.join(os.getcwd(), 'data.py'), 'w') as f:
        f.write(BASE_FCT_DATA_STRING) if TABLE_TYPE == 'fct' else f.write(BASE_DIM_DATA_STRING)
        for endpoint in ENDPOINTS:
            f.write(DATA_DICT[endpoint])
    os.chdir('..')


def generate_model_layer() -> None:
    """Generates the model layer files needed for the new service."""
    print(f'Generating model layer...')
    os.chdir('./model_layer')
    generate_init_file()

    with open(os.path.join(os.getcwd(), 'api_schemas.py'), 'w') as f:
        f.write(BASE_API_SCHEMA_STRING)
        for endpoint in ENDPOINTS:
            if endpoint in VALID_SCHEMA_ENDPOINTS:
                f.write(API_SCHEMA_DICT[endpoint])

    with open(os.path.join(os.getcwd(), 'data_schemas.py'), 'w') as f:
        if TABLE_TYPE == 'fct':
            f.write(
                f'"""Data schemas for the {SERVICE_NAME} service."""\n'
                "from marshmallow import fields, Schema, EXCLUDE\n"
                "\n"
                "\n"
                f"class {CAMEL_CASE_SERVICE_NAME}Schema(Schema):\n"\
                f'    """Base data schema for a {PLAIN_DATA_TYPE}."""\n'
                "    id = fields.UUID(required=True)\n"
                "    # add any attributes\n"
                "\n"
                "    class Meta:\n"
                "        unknown = EXCLUDE\n"
                "\n"
                "\n"
                f"class Populated{CAMEL_CASE_SERVICE_NAME}Schema(Schema):\n"
                f'    """Populated data schema for a {PLAIN_DATA_TYPE}."""\n'
                "    id = fields.UUID(required=True)\n"
                "    # add any attributes\n"
                "\n"
                "    class Meta:\n"
                "        unknown = EXCLUDE\n"
                "\n"
            )
        elif TABLE_TYPE == 'dim':
            f.write(
                f'"""Data schemas for the {SERVICE_NAME} service."""\n'
                "from marshmallow import fields, Schema, EXCLUDE\n"
                "\n"
                "\n"
                f"class {CAMEL_CASE_SERVICE_NAME}Schema(Schema):\n"
                f'    """Base data schema for a {PLAIN_DATA_TYPE}."""\n'
                "    id = fields.UUID(required=True)\n"
                "    # add any attributes\n"
                "\n"
                "    class Meta:\n"
                "        unknown = EXCLUDE\n"
                "\n"
            )
        else:
            print(f'Invalid table_type {TABLE_TYPE}. Failed to populate data schemas.')
    os.chdir('..')


### File Templates ###
### API Layer Templates ###
BASE_API_STRING = (
    f'"""API layer for the {SERVICE_NAME} service."""\n'
    "from typing import Optional\n"
    '\n'
    "from chalice import Blueprint\n"
    '\n'
    f'from restless_services.{SERVICE_NAME}.business_layer import business\n'
    f'from restless_services.{SERVICE_NAME}.model_layer.api_schemas import (\n'
    f'{SCHEMA_IMPORT_STRING}'
    ')\n'
    "from utils.api_handler import api_handler\n"
    '\n'
    "api = Blueprint(__name__)\n"
    '\n'
)


API_CREATE_STRING = (
    '\n'
    '@api_handler(\n'
    '    api=api,\n'
    f'    path="/{SERVICE_NAME}",\n'
    '    methods=["POST"],\n'
    f'    body_schema=Create{CAMEL_CASE_DATA_TYPE}BodySchema,\n'
    ")\n"
    f'def create_{DATA_TYPE}() -> Optional[dict]:\n'
    f'    """Creates a new {PLAIN_DATA_TYPE} in the {TABLE_TYPE}_{SERVICE_NAME} table.\n'
    "\n"
    "    Returns:\n"
    f'        A newly created {PLAIN_DATA_TYPE} else None.\n'
    '    """\n'
    f'    return business.create_{DATA_TYPE}(\n'
    '        # pass in variables\n'
    '    )\n'
    '\n'
)


API_GET_STRING = (
    '\n'
    '@api_handler(\n'
    '    api=api,\n'
    f'    path="/{SERVICE_NAME}",\n'
    '    methods=["GET"],\n'
    f'    query_schema=Get{CAMEL_CASE_SERVICE_NAME}QuerySchema,\n'
    ")\n"
    f'def get_{SERVICE_NAME}() -> list:\n'
    f'    """Gets {PLAIN_SERVICE_NAME} from the {TABLE_TYPE}_{SERVICE_NAME} table filtered by given params.\n'
    "\n"
    "    Returns:\n"
    f'        A list of {PLAIN_SERVICE_NAME} filtered by any given params.\n'
    '    """\n'
    f'    return business.get_{SERVICE_NAME}(\n'
    '        # pass in variables\n'
    '    )\n'
    '\n'
)


API_GET_BY_ID_STRING = (
    '\n'
    '@api_handler(\n'
    '    api=api,\n'
    f'    path="/{SERVICE_NAME}/{{{DATA_TYPE}_id}}",\n'
    '    methods=["GET"],\n'
    ")\n"
    f'def get_{DATA_TYPE}_by_id({DATA_TYPE}_id: str) -> Optional[dict]:\n'
    f'    """Gets a {PLAIN_DATA_TYPE} from the {TABLE_TYPE}_{SERVICE_NAME} table by the given id.\n'
    "\n"
    "    Args:\n"
    f'        {DATA_TYPE}_id - The primary key of a {PLAIN_DATA_TYPE} in the {TABLE_TYPE}_{SERVICE_NAME} table.\n'
    "\n"
    "    Returns:\n"
    f'        A {PLAIN_DATA_TYPE} with the given id else None.\n'
    '    """\n'
    f'    return business.get_{DATA_TYPE}_by_id({DATA_TYPE}_id={DATA_TYPE}_id)\n'
    '\n'
)


API_UPDATE_STRING = (
    '\n'
    '@api_handler(\n'
    '    api=api,\n'
    f'    path="/{SERVICE_NAME}/'
    f'{{{DATA_TYPE}_id}}",\n'
    '    methods=["PATCH"],\n'
    f'    body_schema=Update{CAMEL_CASE_DATA_TYPE}BodySchema,\n'
    ")\n"
    f'def update_{DATA_TYPE}({DATA_TYPE}_id: str) -> Optional[dict]:\n'
    f'    """Updates a {PLAIN_DATA_TYPE} in the {TABLE_TYPE}_{SERVICE_NAME} table by the given id.\n'
    "\n"
    "    Args:\n"
    f'        {DATA_TYPE}_id - The primary key of a {PLAIN_DATA_TYPE} in the {TABLE_TYPE}_{SERVICE_NAME} table.\n'
    "\n"
    "    Returns:\n"
    f'        An updated {PLAIN_DATA_TYPE} with the given id else None.\n'
    '    """\n'
    f'    return business.update_{DATA_TYPE}(\n'
    f'        {DATA_TYPE}_id={DATA_TYPE}_id,\n'
    '        # pass in variables\n'
    '    )\n'
    '\n'
)


API_DELETE_STRING = (
    '\n'
    '@api_handler(\n'
    '    api=api,\n'
    f'    path="/{SERVICE_NAME}",\n'
    '    methods=["DELETE"],\n'
    f'    query_schema=Delete{CAMEL_CASE_SERVICE_NAME}QuerySchema,\n'
    ")\n"
    f'def delete_{SERVICE_NAME}() -> list:\n'
    f'    """Deletes {PLAIN_SERVICE_NAME} from the {TABLE_TYPE}_{SERVICE_NAME} table using given params.\n'
    "\n"
    "    Returns:\n"
    f'        A list of {PLAIN_SERVICE_NAME} deleted using given params.\n'
    '    """\n'
    f'    return business.delete_{SERVICE_NAME}(\n'
    '        # pass in variables\n'
    '    )\n'
    '\n'
)


API_DELETE_BY_ID_STRING = (
    '\n'
    '@api_handler(\n'
    '    api=api,\n'
    f'    path="/{SERVICE_NAME}/{{{DATA_TYPE}_id}}",\n'
    '    methods=["DELETE"],\n'
    ")\n"
    f'def delete_{DATA_TYPE}_by_id({DATA_TYPE}_id: str) -> Optional[dict]:\n'
    f'    """Deletes a {PLAIN_DATA_TYPE} from the {TABLE_TYPE}_{SERVICE_NAME} table by the given id.\n'
    "\n"
    "    Args:\n"
    f'        {DATA_TYPE}_id - The primary key of a {PLAIN_DATA_TYPE} in the {TABLE_TYPE}_{SERVICE_NAME} table.\n'
    "\n"
    "    Returns:\n"
    f'        A deleted {PLAIN_DATA_TYPE} with the given id else None.\n'
    '    """\n'
    f'    return business.delete_{DATA_TYPE}_by_id({DATA_TYPE}_id={DATA_TYPE}_id)\n'
    '\n'
)


API_DICT = {
    'POST': API_CREATE_STRING,
    'GET': API_GET_STRING,
    'GET_BY_ID': API_GET_BY_ID_STRING,
    'PATCH': API_UPDATE_STRING,
    'DELETE': API_DELETE_STRING,
    'DELETE_BY_ID': API_DELETE_BY_ID_STRING,
}


### Business Layer Templates ###
BASE_BUSINESS_STRING = (
    f'"""Business layer for the {SERVICE_NAME} service."""\n'
    "from typing import Optional\n"
    "\n"
    "from utils.types import UUIDType\n"
    "from utils.validation import validate_params\n"
    f'from restful_services.{SERVICE_NAME}.data_layer import data\n'
    "\n"
)


BUSINESS_CREATE_STRING = (
    "\n"
    f'def create_{DATA_TYPE}(\n'
    "    # pass in variables\n"
    ') -> Optional[dict]:\n'
    f'    """Creates a new {PLAIN_DATA_TYPE} in the {TABLE_TYPE}_{SERVICE_NAME} table.\n'
    "\n"
    "    Args:\n"
    "        # list any given params here\n"
    "\n"
    "    Returns:\n"
    f'        A newly created {PLAIN_DATA_TYPE} else None.\n'
    "\n"
    "    Raises:\n"
    "        InvalidParamException - If any of the given params are None.\n"
    '    """\n'
    "    validate_params(\n"
    f"        func='create_{DATA_TYPE}',\n"
    "        params={\n"
    "            # pass required params here\n"
    "        },\n"
    "    )\n"
    f"    return data.create_{DATA_TYPE}(\n"
    "        # pass in variables\n"
    "    )\n"
    "\n"
)


BUSINESS_GET_STRING = (
    "\n"
    f'def get_{SERVICE_NAME}(\n'
    "    # pass in variables\n"
    ') -> list:\n'
    f'    """Gets {PLAIN_SERVICE_NAME} from the {TABLE_TYPE}_{SERVICE_NAME} table filtered by given params.\n'
    "\n"
    "    Args:\n"
    "        # list any given params here\n"
    "\n"
    "    Returns:\n"
    f'        A list of {PLAIN_SERVICE_NAME} filtered by any given params.\n'
    '    """\n'
    f"    return data.get_{SERVICE_NAME}()\n"
    "\n"
)


BUSINESS_GET_BY_ID_STRING = (
    "\n"
    f'def get_{DATA_TYPE}_by_id({DATA_TYPE}_id: UUIDType) -> Optional[dict]:\n'
    f'    """Gets a {PLAIN_DATA_TYPE} from the {TABLE_TYPE}_{SERVICE_NAME} table by the given id.\n'
    "\n"
    "    Args:\n"
    f'        {DATA_TYPE}_id - The primary key of a {PLAIN_DATA_TYPE} in the {TABLE_TYPE}_{SERVICE_NAME} table.\n'
    "\n"
    "    Returns:\n"
    f'        A {PLAIN_DATA_TYPE} with the given id else None.\n'
    "\n"
    "    Raises:\n"
    f"        InvalidParamException - If the given {DATA_TYPE}_id is None.\n"
    '    """\n'
    "    validate_params(\n"
    f"        func='get_{DATA_TYPE}_by_id',\n"
    f"        params={{'{DATA_TYPE}_id': {DATA_TYPE}_id}},\n"
    "    )\n"
    f"    return data.get_{DATA_TYPE}_by_id({DATA_TYPE}_id={DATA_TYPE}_id)\n"
    "\n"
)


BUSINESS_UPDATE_STRING = (
    "\n"
    f'def update_{DATA_TYPE}(\n'
    f'    {DATA_TYPE}_id: UUIDType,\n'
    "    # pass any other given params\n"
    ') -> Optional[dict]:\n'
    f'    """Updates a {PLAIN_DATA_TYPE} in the {TABLE_TYPE}_{SERVICE_NAME} table by the given id.\n'
    "\n"
    "    Args:\n"
    f'        {DATA_TYPE}_id - The primary key of a {PLAIN_DATA_TYPE} in the {TABLE_TYPE}_{SERVICE_NAME} table.\n'
    "        # list any other given params here\n"
    "\n"
    "    Returns:\n"
    f'        An updated {PLAIN_DATA_TYPE} with the given id else None.\n'
    "\n"
    "    Raises:\n"
    f"        InvalidParamException - If any of the given params or the {DATA_TYPE}_id is None.\n"
    '    """\n'
    "    validate_params(\n"
    f"        func='update_{DATA_TYPE}',\n"
    f"        params={{\n"
    f"            '{DATA_TYPE}_id': {DATA_TYPE}_id,\n"
    "            # pass other required params here\n"
    "        }\n"
    "    )\n"
    f"    return data.update_{DATA_TYPE}(\n"
    f"        {DATA_TYPE}_id={DATA_TYPE}_id,\n"
    "        # pass any other given params\n"
    "    )\n"
    "\n"
)


BUSINESS_DELETE_STRING = (
    "\n"
    f'def delete_{SERVICE_NAME}(\n'
    "    # pass any given params\n"
    ') -> list:\n'
    f'    """Deletes {PLAIN_SERVICE_NAME} from the {TABLE_TYPE}_{SERVICE_NAME} table using given params.\n'
    "\n"
    "    Args:\n"
    "        # list any given params here\n"
    "\n"
    "    Returns:\n"
    f'        A list of {PLAIN_SERVICE_NAME} deleted using given params.\n'
    '    """\n'
    f"    return data.delete_{SERVICE_NAME}(\n"
    "        # pass any other given params\n"
    "    )\n"
    "\n"
)


BUSINESS_DELETE_BY_ID_STRING = (
    "\n"
    f'def delete_{DATA_TYPE}_by_id({DATA_TYPE}_id: UUIDType) -> Optional[dict]:\n'
    f'    """Deletes a {PLAIN_DATA_TYPE} from the {TABLE_TYPE}_{SERVICE_NAME} table by the given id.\n'
    "\n"
    "    Args:\n"
    f'        {DATA_TYPE}_id - The primary key of a {PLAIN_DATA_TYPE} in the {TABLE_TYPE}_{SERVICE_NAME} table.\n'
    "\n"
    "    Returns:\n"
    f'        A deleted {PLAIN_DATA_TYPE} with the given id else None.\n'
    "\n"
    "    Raises:\n"
    f"        InvalidParamException - If the given {DATA_TYPE}_id is None.\n"
    '    """\n'
    "    validate_params(\n"
    f"        func='delete_{DATA_TYPE}_by_id',\n"
    f"        params={{'{DATA_TYPE}_id': {DATA_TYPE}_id}},\n"
    "    )\n"
    f"    return data.delete_{DATA_TYPE}_by_id({DATA_TYPE}_id={DATA_TYPE}_id)\n"
    "\n"
)


BUSINESS_DICT = {
    'POST': BUSINESS_CREATE_STRING,
    'GET': BUSINESS_GET_STRING,
    'GET_BY_ID': BUSINESS_GET_BY_ID_STRING,
    'PATCH': BUSINESS_UPDATE_STRING,
    'DELETE': BUSINESS_DELETE_STRING,
    'DELETE_BY_ID': BUSINESS_DELETE_BY_ID_STRING,
}


### Data Layer Templates ###
BASE_FCT_DATA_STRING = (
    f'"""Data layer for the {SERVICE_NAME} service."""\n'
    "from typing import Optional\n"
    "\n"
    f"from db_models.{TABLE_TYPE}_{SERVICE_NAME} import {TABLE_TYPE.capitalize()}{CAMEL_CASE_SERVICE_NAME}\n"
    "from utils import db\n"
    "from utils.types import UUIDType\n"
    f"from restful_services.{SERVICE_NAME}.model_layer.data_schemas import (\n"
    f"    {CAMEL_CASE_SERVICE_NAME}Schema,\n"
    f"    Populated{CAMEL_CASE_SERVICE_NAME}Schema,\n"
    f")\n"
    "\n"
)


BASE_DIM_DATA_STRING = (
    f'"""Data layer for the {SERVICE_NAME} service."""\n'
    "from typing import Optional\n"
    "\n"
    f"from db_models.{TABLE_TYPE}_{SERVICE_NAME} import {TABLE_TYPE.capitalize()}{CAMEL_CASE_SERVICE_NAME}\n"
    "from utils import db\n"
    "from utils.types import UUIDType\n"
    f"from restful_services.{SERVICE_NAME}.model_layer.data_schemas import {CAMEL_CASE_SERVICE_NAME}Schema\n"
    "\n"
)


DATA_CREATE_STRING = (
    "\n"
    f'def create_{DATA_TYPE}(\n'
    "    # pass in variables\n"
    ') -> Optional[dict]:\n'
    f'    """Creates a new {PLAIN_DATA_TYPE} in the {TABLE_TYPE}_{SERVICE_NAME} table.\n'
    "\n"
    "    Args:\n"
    "        # list any given params here\n"
    "\n"
    "    Returns:\n"
    f'        A newly created {PLAIN_DATA_TYPE} else None.\n'
    '    """\n'
    "    with db.session_scope() as session:\n"
    f"        new_{DATA_TYPE} = {TABLE_TYPE.capitalize()}{CAMEL_CASE_SERVICE_NAME}(\n"
    "            # pass in variables\n"
    "        )\n"
    "\n"
    f"        if new_{DATA_TYPE}:\n"
    f"            session.add(new_{DATA_TYPE})\n"
    "            session.commit()\n"
    f"            return {CAMEL_CASE_SERVICE_NAME}Schema().dump(new_{DATA_TYPE})\n"
    "        return None\n"
    "\n"
)


DATA_GET_STRING = (
    "\n"
    f"def get_{SERVICE_NAME}() -> list:\n"
    f'    """Gets all {PLAIN_SERVICE_NAME} from the {TABLE_TYPE}_{SERVICE_NAME} table.\n'
    "\n"
    "    Returns:\n"
    f'        A list of {PLAIN_SERVICE_NAME}.\n'
    '    """\n'
    "    with db.session_scope() as session:\n"
    f"        {SERVICE_NAME} = session.query({TABLE_TYPE.capitalize()}{CAMEL_CASE_SERVICE_NAME}).all()\n"
    f"        return Populated{CAMEL_CASE_SERVICE_NAME}Schema().dump({SERVICE_NAME}) if {SERVICE_NAME} else []\n"
    "\n"
)


DATA_GET_BY_ID_STRING = (
    "\n"
    f"def get_{DATA_TYPE}_by_id({DATA_TYPE}_id: UUIDType) -> Optional[dict]:\n"
    f'    """Gets a {PLAIN_DATA_TYPE} from the {TABLE_TYPE}_{SERVICE_NAME} table by the given id.\n'
    "\n"
    "    Args:\n"
    f'        {DATA_TYPE}_id - The primary key of a {PLAIN_DATA_TYPE} in the {TABLE_TYPE}_{SERVICE_NAME} table.\n'
    "\n"
    "    Returns:\n"
    f'        A {PLAIN_DATA_TYPE} with the given id else None.\n'
    '    """\n'
    "    with db.session_scope() as session:\n"
    f"        {DATA_TYPE} = session.query({TABLE_TYPE.capitalize()}{CAMEL_CASE_SERVICE_NAME}).filter_by(id={DATA_TYPE}_id).one_or_none()\n"
    f"        return Populated{CAMEL_CASE_SERVICE_NAME}Schema().dump({DATA_TYPE}) if {DATA_TYPE} else None\n"
    "\n"
)


DATA_UPDATE_STRING = (
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
    f"        {DATA_TYPE} = session.query({TABLE_TYPE.capitalize()}{CAMEL_CASE_SERVICE_NAME}).filter_by(id={DATA_TYPE}_id).one_or_none()\n"
    "\n"
    f"        if {DATA_TYPE}:\n"
    "            # update entity\n"
    "            session.commit()\n"
    f"            return {CAMEL_CASE_SERVICE_NAME}Schema().dump({DATA_TYPE})\n"
    "        return None\n"
    "\n"
)


DATA_DELETE_STRING = (
    "\n"
    f'def delete_{SERVICE_NAME}(\n'
    "    # pass any given params\n"
    ') -> list:\n'
    f'    """Deletes {PLAIN_SERVICE_NAME} from the {TABLE_TYPE}_{SERVICE_NAME} table using given params.\n'
    "\n"
    "    Args:\n"
    "        # list any given params here\n"
    "\n"
    "    Returns:\n"
    f'        A list of {PLAIN_SERVICE_NAME} deleted using given params.\n'
    '    """\n'
    "    with db.session_scope() as session:\n"
    f"        {SERVICE_NAME} = session.query({TABLE_TYPE.capitalize()}{CAMEL_CASE_SERVICE_NAME}).filter_by().all()\n"
    "\n"
    f"        if {SERVICE_NAME}:\n"
    f"            for {DATA_TYPE} in {SERVICE_NAME}:\n"
    f"                session.delete({DATA_TYPE})\n"
    "                session.commit()\n"
    f"                return {CAMEL_CASE_SERVICE_NAME}Schema().dump({SERVICE_NAME})\n"
    "        return []\n"
    "\n"
)


DATA_DELETE_BY_ID_STRING = (
    "\n"
    f"def delete_{DATA_TYPE}_by_id({DATA_TYPE}_id: UUIDType) -> Optional[dict]:\n"
    f'    """Deletes a {PLAIN_DATA_TYPE} from the {TABLE_TYPE}_{SERVICE_NAME} table by the given id.\n'
    "\n"
    "    Args:\n"
    f'        {DATA_TYPE}_id - The primary key of a {PLAIN_DATA_TYPE} in the {TABLE_TYPE}_{SERVICE_NAME} table.\n'
    "\n"
    "    Returns:\n"
    f'        A deleted {PLAIN_DATA_TYPE} with the given id else None.\n'
    '    """\n'
    "    with db.session_scope() as session:\n"
    f"        {DATA_TYPE} = session.query({TABLE_TYPE.capitalize()}{CAMEL_CASE_SERVICE_NAME}).filter_by(id={DATA_TYPE}_id).one_or_none()\n"
    "\n"
    f"        if {DATA_TYPE}:\n"
    f"            session.delete({DATA_TYPE})\n"
    "            session.commit()\n"
    f"            return {CAMEL_CASE_SERVICE_NAME}Schema().dump({DATA_TYPE})\n"
    "        return None\n"
    "\n"
)


DATA_DICT = {
    'POST': DATA_CREATE_STRING,
    'GET': DATA_GET_STRING,
    'GET_BY_ID': DATA_GET_BY_ID_STRING,
    'PATCH': DATA_UPDATE_STRING,
    'DELETE': DATA_DELETE_STRING,
    'DELETE_BY_ID': DATA_DELETE_BY_ID_STRING,
}


### Model Layer Templates ###
BASE_API_SCHEMA_STRING = (
    f'"""API schemas for the {SERVICE_NAME} service."""\n'
    "from marshmallow import fields, Schema\n"
    "\n"
)


API_SCHEMA_CREATE_STRING = (
    "\n"
    f"class Create{CAMEL_CASE_DATA_TYPE}BodySchema:\n"
    f'    """Schema for creating a new {PLAIN_DATA_TYPE}."""\n'
    "    pass # TODO - set expected values\n"
    "\n"
)


API_SCHEMA_GET_STRING = (
    "\n"
    f"class Get{CAMEL_CASE_SERVICE_NAME}QuerySchema:\n"
    f'    """Schema for getting {PLAIN_SERVICE_NAME}."""\n'
    "    pass # TODO - set expected values\n"
    "\n"
)


API_SCHEMA_UPDATE_STRING = (
    "\n"
    f"class Update{CAMEL_CASE_DATA_TYPE}BodySchema:\n"
    f'    """Schema for updating a {PLAIN_DATA_TYPE}."""\n'
    "    pass # TODO - set expected values\n"
    "\n"
)


API_SCHEMA_DELETE_STRING = (
    "\n"
    f"class Delete{CAMEL_CASE_SERVICE_NAME}QuerySchema:\n"
    f'    """Schema for deleting {PLAIN_SERVICE_NAME}."""\n'
    "    pass # TODO - set expected values\n"
    "\n"
)


API_SCHEMA_DICT = {
    'POST': API_SCHEMA_CREATE_STRING,
    'GET': API_SCHEMA_GET_STRING,
    'PATCH': API_SCHEMA_UPDATE_STRING,
    'DELETE': API_SCHEMA_DELETE_STRING,
}


if __name__ == "__main__":
    main()
