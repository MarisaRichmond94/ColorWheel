"""Functions for generating model layer files."""
import argparse
import os

from helpers import generate_init_file


def generate_model_layer(
    api_schemas_template,
    data_schemas_template,
    args: argparse.Namespace
) -> None:
    """Generates the data layer files needed for the new service.

    Args:
        api_schemas_template: A jinja2 template used to generate the api_schemas python file.
        data_schemas_template: A jinja2 template used to generate the data_schemas python file.
        args - An object containing attributes parsed out of the command line.
    """
    print('Generating model layer...')
    os.chdir('./model_layer')
    generate_init_file()
    if any(method in args.valid_api_schema_methods for method in args.methods):
        with open(os.path.join(os.getcwd(), 'api_schemas.py'), 'w') as file:
            file.write(api_schemas_template.render(args=args, imports=determine_file_imports(args)))
    with open(os.path.join(os.getcwd(), 'data_schemas.py'), 'w') as file:
        file.write(data_schemas_template.render(args=args))
    os.chdir('..')


def determine_file_imports(args: argparse.Namespace) -> list:
    """Dynamically generates a list of api imports using the given command line parsed args.

    Args:
        args: An object containing attributes parsed out of the command line.

    Returns:
        A list of imports needed for the given file.
    """
    return ['from marshmallow import fields, Schema']
