"""Functions for generating api layer files."""
import argparse
import os

from utils.common import generate_init_file


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
        file.write(template.render(args=args, imports=determine_file_imports(args)))
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

    optional_methods = ['POST', 'GET_BY_ID', 'PATCH', 'DELETE', 'DELETE_BY_ID']
    if any(method in optional_methods for method in args.methods):
        imports.append('from typing import Optional')
        imports.append('')

    imports = imports + [
        'from chalice import Blueprint',
        '',
        f'from restful_services.{args.plural_service_name}.business_layer import business'
    ]

    api_schema_imports = determine_api_schema_import_funcs(args)
    if api_schema_imports:
        if len(api_schema_imports) == 1:
            imports.append(
                f'from restful_services.{args.plural_service_name}.model_layer.api_schemas import '
                f'{api_schema_imports[0]}'
            )
        else:
            imports.append(
                f'from restful_services.{args.plural_service_name}.model_layer.api_schemas import ('
            )
            for api_schema_import in api_schema_imports:
                imports.append(f'    {api_schema_import}')
            imports.append(')')

    if args.method_permissions:
        all_permissions = [
            required_permissions
            for method_permissions in args.method_permissions.values()
            for required_permissions in method_permissions.get("required_permissions_upper")
        ]
        unique_sorted_permissions = sorted(list(set(all_permissions)))
        permissions_string = ''
        for permission in unique_sorted_permissions:
            permissions_string += f' {permission},'
        imports.append(
            f'from settings.permissions import {permissions_string.rstrip(permissions_string[-1])}'
        )

    imports.append('from utils.api_handler import api_handler')

    return imports
