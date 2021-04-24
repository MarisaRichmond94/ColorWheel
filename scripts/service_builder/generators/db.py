"""Functions for generating data layer files."""
import argparse
import os

from helpers import generate_init_file


def generate_database_model(template, args: argparse.Namespace) -> None:
    """Generates the db_model file needed for the new service.

    Args:
        template: A jinja2 template used to generate the python file.
        args - An object containing attributes parsed out of the command line.
    """
    print('Generating database model...')
    os.chdir('../../db_models')
    generate_init_file()
    db_model_file_name = f'{args.table_type}_{args.plural_service_name}.py'
    with open(os.path.join(os.getcwd(), db_model_file_name), 'w') as file:
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

    sqlalchemy_types = ['Column'] if args.table_type == 'fct' else ['Column', 'ForeignKey']
    if args.dimensions:
        sqlalchemy_types = sqlalchemy_types + [args.dimensions[key]['sqlalchemy_type'] for key in args.dimensions]
        sqlalchemy_types = list(set(sqlalchemy_types))
        sqlalchemy_types.sort()
    sqlalchemy_imports = ', '.join(sqlalchemy_types)
    imports.append(f'from sqlalchemy import {sqlalchemy_imports}')

    if args.table_type == 'fct':
        imports.append('')
        imports.append('from db_models.base_model import Base')
        if args.foreign_dims:
            for key in args.foreign_dims:
                plural_service_name = args.foreign_dims.get(key).get('plural')
                schema = args.foreign_dims.get(key).get('plural_schema')
                imports.append(
                    f'from db_models.dim_{plural_service_name} import Dim{schema}'
                )
    else:
        imports = imports + [
            'from sqlalchemy.orm import relationship',
            'from sqlalchemy.dialects.postgresql import UUID',
            '',
            'from db_models.base_model import Base'
        ]

    return imports
