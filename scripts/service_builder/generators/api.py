"""Functions for generating api layer files."""
import argparse
import os

from helpers import generate_init_file


def generate_api_layer(template, args: argparse.Namespace) -> None:
    """Generates the api layer files needed for the new service.

    Args:
        template: A jinja2 template used to generate the python file.
        args: An object containing attributes parsed out of the command line.
    """
    print('Generating api layer...')
    os.chdir('./api_layer')
    generate_init_file()
    with open(os.path.join(os.getcwd(), 'api.py'), 'w') as file:
        file.write(
            template.render(
                args=args,
                api_schema_import_funcs=determine_api_schema_import_funcs(args),
                imports=determine_file_imports(args),
            )
        )
    os.chdir('..')


def determine_api_schema_import_funcs(args: argparse.Namespace) -> str:
    """Dynamically generates a schema import string based on methods requiring a schema.

    Args:
        args: An object containing attributes parsed out of the command line.

    Returns:
        An import string based on required methods else an empty string.
    """
    api_schema_import_dict = {
        'POST': f"Create{args.singular_schema_name}BodySchema",
        'GET': f"Get{args.plural_schema_name}QuerySchema",
        'PATCH': f"Update{args.singular_schema_name}BodySchema",
        'DELETE': f"Delete{args.plural_schema_name}QuerySchema"
    }
    api_schema_import_funcs = []
    valid_api_schema_methods = args.valid_api_schema_methods.split(' ')
    for method in args.methods:
        if method in valid_api_schema_methods:
            api_schema_import_funcs.append(f'{api_schema_import_dict[method]},')
    if len(api_schema_import_funcs) > 0:
        api_schema_import_funcs.sort()
        api_schema_import_funcs[-1] = api_schema_import_funcs[-1][:-1]
    return api_schema_import_funcs


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

    return imports + [
        'from chalice import Blueprint',
        '',
        'from restful_services.{{args.plural_service_name}}.business_layer import business',
    ]
