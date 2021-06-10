#!/usr/bin/python
import os
import sys

from jinja2 import Environment, FileSystemLoader

from generators.alembic_migration import generate_alembic_migration_command
from generators.api import generate_api_layer
from generators.business import generate_business_layer
from generators.data import generate_data_layer
from generators.models import generate_model_layer
from generators.db import generate_database_model, populate_alembic_env_with_db_model
from utils.create.service_folders import create_restful_service_folders
from utils.populate.method_permissions import populate_method_permissions
from utils.populate.root_app import populate_root_app_with_new_api_routes
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
    'db_model': JINJA_ENV.get_template('db_model.py.j2')
}


def main() -> None:
    """Generates a new service package using arguments parsed from the command line as inputs."""
    args = parse_command_line_options()
    navigate_to_restful_services()
    populate_root_app_with_new_api_routes(args=args)
    create_restful_service_folders(args)
    if args.generate_api_layer:
        generate_api_layer(template=TEMPLATE_DICT['api'], args=args)
    generate_business_layer(template=TEMPLATE_DICT['business'], args=args)
    generate_data_layer(template=TEMPLATE_DICT['data'], args=args)
    generate_model_layer(
        api_schemas_template=TEMPLATE_DICT['api_schemas'],
        data_schemas_template=TEMPLATE_DICT['data_schemas'],
        args=args
    )
    generate_database_model(template=TEMPLATE_DICT['db_model'], args=args)
    if args.method_permissions:
        populate_method_permissions(args.method_permissions)
    populate_alembic_env_with_db_model(args=args)
    alembic_migration_command = generate_alembic_migration_command(args=args)
    print(f"**DON'T FORGET TO GENERATE YOUR SQL MIGRATION: `{alembic_migration_command}`**")
    print(f'Successfully generated {args.plural_service_name} service! (っ＾▿＾)۶🍸🌟🍺٩(˘◡˘ )')


def navigate_to_restful_services() -> None:
    """Navigates to the restless_services or the restful_services folder depending on inputs."""
    current_working_directory = os.getcwd().split('/')[-1]
    if current_working_directory not in ('api', 'restful_services'):
        print("Please run from the api folder or the restful_services folder.")
        sys.exit()

    if current_working_directory == 'api':
        print("Changing directories to restful_services...")
        os.chdir('./chalicelib/restful_services')


if __name__ == "__main__":
    main()
