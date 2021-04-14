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

    if any(method in ['POST', 'GET_BY_ID', 'PATCH', 'DELETE_BY_ID'] for method in args.methods):
        imports.append('from typing import Optional')
        imports.append('')

    imports.append(f'from restful_services.{{args.plural_service_name}}.data_layer import data')

    if any(method in ['GET_BY_ID', 'PATCH', 'DELETE_BY_ID'] for method in args.methods):
        imports.append('from utils.types import UUIDType')

    if any(method in ['POST', 'GET_BY_ID', 'PATCH', 'DELETE_BY_ID'] for method in args.methods):
        imports.append('from utils.validation import validate_params')

    return imports
