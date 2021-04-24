#!/usr/bin/python
import argparse
import os
import sys

from jinja2 import Environment, FileSystemLoader

from generators.api import generate_api_layer
from generators.business import generate_business_layer
from generators.data import generate_data_layer
from generators.models import generate_model_layer
from generators.db import generate_database_model
from helpers import generate_init_file
from setup import parse_command_line_options

JINJA_ENV = Environment(
    loader=FileSystemLoader(searchpath=os.path.join(os.path.dirname(__file__), 'templates')),
    lstrip_blocks=True,
    trim_blocks=True
)
TEMPLATE_DICT = {
    'api': JINJA_ENV.get_template('api.py.j2'),
    'api_schemas': JINJA_ENV.get_template('api_schemas.py.j2'),
    'business': JINJA_ENV.get_template('business.py.j2'),
    'data': JINJA_ENV.get_template('data.py.j2'),
    'data_schemas': JINJA_ENV.get_template('data_schemas.py.j2'),
    'db_model': JINJA_ENV.get_template('db_model.py.j2'),
}


def main() -> None:
    """Generates a new service package using arguments parsed from the command line as inputs."""
    args = parse_command_line_options()
    navigate_to_restful_services()
    create_folders_and_inits(args)
    generate_api_layer(template=TEMPLATE_DICT['api'], args=args)
    generate_business_layer(template=TEMPLATE_DICT['business'], args=args)
    generate_data_layer(template=TEMPLATE_DICT['data'], args=args)
    generate_model_layer(
        api_schemas_template=TEMPLATE_DICT['api_schemas'],
        data_schemas_template=TEMPLATE_DICT['data_schemas'],
        args=args
    )
    generate_database_model(template=TEMPLATE_DICT['db_model'], args=args)
    print(f'Successfully generated {args.plural_service_name} service! (っ＾▿＾)۶🍸🌟🍺٩(˘◡˘ )')
    print(
        "**DON'T FORGET TO ADD THE ROUTE TO APP.PY, IMPORT DB_MODEL INTO ENV.PY, "
        "AND GENERATE YOUR SQL MIGRATION**"
    )


def navigate_to_restful_services() -> None:
    """Navigates to the restless_services or the restful_services folder depending on inputs."""
    current_working_directory = os.getcwd().split('/')[-1]
    if current_working_directory not in ('api', 'restful_services'):
        print("Please run from the api folder or the restful_services folder.")
        sys.exit()

    if current_working_directory == 'api':
        print("Changing directories to restful_services...")
        os.chdir('./chalicelib/restful_services')


def create_folders_and_inits(args: argparse.Namespace) -> None:
    """Creates all of the base-level folders needed for the new service given a valid name.

    Args:
        args - An object containing attributes parsed out of the command line.
    """
    print(f'Generating new service with name {args.plural_service_name}...')
    os.mkdir(f'./{args.plural_service_name}')
    os.chdir(f'./{args.plural_service_name}')
    generate_init_file()
    os.mkdir('./api_layer')
    os.mkdir('./business_layer')
    os.mkdir('./data_layer')
    os.mkdir('./model_layer')


if __name__ == "__main__":
    main()
