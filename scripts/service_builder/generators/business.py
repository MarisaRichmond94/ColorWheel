"""Functions for generating business layer files."""
import argparse
import os

from helpers import generate_init_file


def generate_business_layer(template, args: argparse.Namespace) -> None:
    """Generates the business layer files needed for the new service.

    Args:
        template: A jinja2 template used to generate the python file.
        args - An object containing attributes parsed out of the command line.
    """
    print('Generating business layer...')
    os.chdir('./business_layer')
    generate_init_file()
    with open(os.path.join(os.getcwd(), 'business.py'), 'w') as file:
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

    should_import_optional = determine_should_import_optional(args)
    if should_import_optional:
        imports.append('from typing import Optional')
        imports.append('')

    imports.append(
        f'from restful_services.{args.plural_service_name}.data_layer import data'
    )

    should_import_uuidtype = determine_should_import_uuidtype(args)
    if should_import_uuidtype:
        imports.append('from utils.types import UUIDType')

    if any(method in ['POST', 'GET_BY_ID', 'PATCH', 'DELETE_BY_ID'] for method in args.methods):
        imports.append('from utils.validation import validate_params')

    return imports


def determine_should_import_optional(args: argparse.Namespace) -> bool:
    """Determines whether or not a file needs the typings Optional library.

    Args:
        args: An object containing attributes parsed out of the command line.

    Returns:
        A bool representing whether or not a file should import the typings Optional library.
    """
    optional_methods = ['POST', 'GET_BY_ID', 'PATCH', 'DELETE', 'DELETE_BY_ID']
    if any(method in optional_methods for method in args.methods):
        return True
    if args.method_args and args.method_args.get('GET'):
        return True
    return False


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
