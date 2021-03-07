#!/usr/bin/python
import os
import sys

from helpers import convert_snake_to_camel, generate_init_file
from settings import set_settings_variables
from templates.api import generate_api_function, generate_api_imports
from templates.api_schemas import generate_api_schema_function, generate_api_schema_imports
from templates.business import generate_business_function, generate_business_imports
from templates.data import generate_data_function, generate_data_imports
from templates.data_schemas import generate_data_schema_file


### Constants ###
SERVICE_NAME = sys.argv[1]
DATA_TYPE = sys.argv[2]
METHODS = sys.argv[4:len(sys.argv)]
ARG_DICT = {
    'data_type': DATA_TYPE,
    'methods': METHODS,
    'plural_param_type': ' '.join(SERVICE_NAME.split('_')),
    'schema_name': convert_snake_to_camel(SERVICE_NAME),
    'schema_type': convert_snake_to_camel(DATA_TYPE),
    'service_name': SERVICE_NAME,
    'singular_param_type': ' '.join(DATA_TYPE.split('_')),
    'table_type': sys.argv[3],
    'valid_api_schema_methods': ['POST', 'GET', 'PATCH', 'DELETE'],
}


### Main Functions ###
def main() -> None:
    """Generates a new service package using given sys.argv inputs."""
    set_settings_variables(arg_dict=ARG_DICT)
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


def generate_api_layer() -> None:
    """Generates the api layer files needed for the new service."""
    print(f'Generating api layer...')
    os.chdir('./api_layer')
    generate_init_file()
    with open(os.path.join(os.getcwd(), 'api.py'), 'w') as f:
        f.write(generate_api_imports())
        for method in METHODS:
            f.write(generate_api_function(method=method))
        f.truncate(f.tell()-1)
    os.chdir('..')


def generate_business_layer() -> None:
    """Generates the business layer files needed for the new service."""
    print(f'Generating business layer...')
    os.chdir('./business_layer')
    generate_init_file()
    with open(os.path.join(os.getcwd(), 'business.py'), 'w') as f:
        f.write(generate_business_imports())
        for method in METHODS:
            f.write(generate_business_function(method=method))
        f.truncate(f.tell()-1)
    os.chdir('..')


def generate_data_layer() -> None:
    """Generates the data layer files needed for the new service."""
    print(f'Generating data layer...')
    os.chdir('./data_layer')
    generate_init_file()
    with open(os.path.join(os.getcwd(), 'data.py'), 'w') as f:
        f.write(generate_data_imports())
        for method in METHODS:
            f.write(generate_data_function(method=method))
        f.truncate(f.tell()-1)
    os.chdir('..')


def generate_model_layer() -> None:
    """Generates the model layer files needed for the new service."""
    print(f'Generating model layer...')
    os.chdir('./model_layer')
    generate_init_file()
    if any(method in ARG_DICT.get('valid_api_schema_methods') for method in METHODS):
        with open(os.path.join(os.getcwd(), 'api_schemas.py'), 'w') as f:
            f.write(generate_api_schema_imports())
            for method in METHODS:
                f.write(generate_api_schema_function(method=method))
            f.truncate(f.tell()-1)
    with open(os.path.join(os.getcwd(), 'data_schemas.py'), 'w') as f:
        f.write(generate_data_schema_file())
        f.truncate(f.tell()-1)
    os.chdir('..')


if __name__ == "__main__":
    main()
