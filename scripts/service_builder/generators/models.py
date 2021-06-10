"""Functions for generating model layer files."""
import argparse
import os

from utils.common import generate_init_file


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
        if (
            len(args.methods) == 1 and args.methods[0] == 'GET' and
            args.method_args and len(args.method_args) == 1 and
            args.method_args.get('GET')
        ):
            print('Skipping api_schemas.py file generation...')
        else:
            with open(os.path.join(os.getcwd(), 'api_schemas.py'), 'w') as file:
                file.write(
                    api_schemas_template.render(
                        args=args, imports=['from marshmallow import fields, Schema']
                    )
                )
    with open(os.path.join(os.getcwd(), 'data_schemas.py'), 'w') as file:
        file.write(data_schemas_template.render(args=args))
    os.chdir('..')
