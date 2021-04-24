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

    optional_methods = ['POST', 'GET_BY_ID', 'PATCH', 'DELETE', 'DELETE_BY_ID']
    if any(method in optional_methods for method in args.methods):
        imports.append('from typing import Optional')
        imports.append('')

    imports.append(
        f'from db_models.{args.table_type}_{args.plural_service_name} import '
        f'{args.table_type.capitalize()}{args.plural_schema_name}'
    )

    if args.table_type == 'fct':
        non_populated_methods = ('POST', 'PATCH', 'DELETE', 'DELETE_BY_ID')
        populated_methods = ('GET', 'GET_BY_ID')
        if not any(method in non_populated_methods for method in args.methods):
            imports.append(
                f'from restful_services.{args.plural_service_name}.model_layer.data_schemas import '
                f'Populated{args.singular_schema_name}Schema'
            )
        elif not any(method in populated_methods for method in args.methods):
            imports.append(
                f'from restful_services.{args.plural_service_name}.model_layer.data_schemas import '
                f'{args.singular_schema_name}Schema'
            )
        else:
            imports.append(
'''from restful_services.{args.plural_service_name}.model_layer.data_schemas import (
    {args.singular_schema_name}Schema,
    Populated{args.singular_schema_name}Schema
)'''.format(args=args)
            )
    else:
        imports.append(
            f'from restful_services.{args.plural_service_name}.model_layer.data_schemas import '
            f'{args.singular_schema_name}Schema'
        )

    imports.append('from utils import db')

    should_import_uuidtype = determine_should_import_uuidtype(args)
    if should_import_uuidtype:
        imports.append('from utils.types import UUIDType')

    return imports


def determine_should_import_uuidtype(args: argparse.Namespace) -> bool:
    """Determines whether or not a file needs the UUIDType.

    Args:
        args: An object containing attributes parsed out of the command line.

    Returns:
        A bool representing whether or not a file should import the UUIDType.
    """
    if any(method in ['POST', 'GET_BY_ID', 'PATCH', 'DELETE_BY_ID'] for method in args.methods):
        return True

    if args.method_args and args.method_args.get('GET'):
        if any(arg.get('type') == 'UUIDType' for arg in args.method_args.get('GET')):
            return True

    if args.method_args and args.method_args.get('DELETE'):
        if any(arg.get('type') == 'UUIDType' for arg in args.method_args.get('DELETE')):
            return True

    return False
