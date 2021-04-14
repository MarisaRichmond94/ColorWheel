"""Functions for generating data layer files."""
import argparse
import os

from helpers import generate_init_file


def generate_data_layer(template, args: argparse.Namespace) -> None:
    """Generates the data layer files needed for the new service.

    Args:
        template: A jinja2 template used to generate the python file.
        args - An object containing attributes parsed out of the command line.
    """
    print('Generating data layer...')
    os.chdir('./data_layer')
    generate_init_file()
    with open(os.path.join(os.getcwd(), 'data.py'), 'w') as file:
        file.write(template.render(args=args, imports=determine_file_imports(args)))
    os.chdir('..')


def determine_file_imports(args: argparse.Namespace) -> list:
    """Dynamically generates a list of imports using the given command line parsed args.

    Args:
        args: An object containing attributes parsed out of the command line.

    Returns:
        A list of imports needed for the given file.
    """
    imports = []
    has_extra_imports = ['POST', 'GET_BY_ID', 'PATCH', 'DELETE_BY_ID']

    if any(method in has_extra_imports for method in args.methods):
        imports.append('from typing import Optional')
        imports.append('')

    imports.append(f'from db_models.{args.table_type}_{args.plural_service_name} import {args.table_type.capitalize()}{args.singular_schema_name}')
    imports.append('from libs.db.session import session_scope')

    if any(method in has_extra_imports for method in args.methods):
        imports.append('from libs.types import UUIDType')

    imports.append(
'''
from restful_services.{args.plural_service_name}.model_layer.data_schemas import (
    {args.singular_schema_name}Schema,
    Populated{args.singular_schema_name}Schema
)
'''.format(args=args)
    ) if args.table_type == 'fct' else imports.append(
        f'from restful_services.{args.plural_service_name}.model_layer.data_schemas import {args.singular_schema_name}Schema'
    )

    return imports
