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
        sqlalchemy_types = sqlalchemy_types + [dim['sqlalchemy_type'] for dim in args.dimensions]
        sqlalchemy_types.sort()
    sqlalchemy_imports = ', '.join(sqlalchemy_types)
    imports.append(f'from sqlalchemy import {sqlalchemy_imports}')

    return (
        imports + [
            '',
            'from db_models.audit_shadow import create_audit_shadow',
            'from db_models.base_model import Base'
        ] if args.table_type == 'fct'
        else imports + [
            'from sqlalchemy.orm import relationship',
            'from sqlalchemy.dialects.postgresql import UUID',
            '',
            'from db_models.base_model import Base'
        ]
    )
