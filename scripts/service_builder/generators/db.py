"""Functions for generating data layer files."""
import argparse
import os

from utils.common import generate_init_file, insert_line_in_alph_order_by_prefix


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

    sqlalchemy_types = (
        ['Column', 'ForeignKey'] if args.table_type == 'dim' or args.dimension else ['Column']
    )
    if args.dimensions:
        sqlalchemy_types = sqlalchemy_types + [args.dimensions[key]['sqlalchemy_type'] for key in args.dimensions]
        sqlalchemy_types = list(set(sqlalchemy_types))
        sqlalchemy_types.sort()
        sqlalchemy_imports = ', '.join(sqlalchemy_types)
        imports.append(f'from sqlalchemy import {sqlalchemy_imports}')

    if args.table_type == 'fct':
        if args.dimension:
            imports = imports + [
                'from sqlalchemy.orm import relationship',
                'from sqlalchemy.dialects.postgresql import UUID'
            ]
            imports.append('')
        imports.append('from db_models.base_model import Base')
        if args.foreign_dims:
            for key in args.foreign_dims:
                plural_service_name = args.foreign_dims.get(key).get('plural')
                schema = args.foreign_dims.get(key).get('plural_schema')
                table_type = args.foreign_dims.get(key).get('table_type')
                imports.append(
                    f'from db_models.{table_type}_{plural_service_name} import '
                    f'{table_type.capitalize()}{schema}'
                )
    else:
        imports = imports + [
            'from sqlalchemy.orm import relationship',
            'from sqlalchemy.dialects.postgresql import UUID',
            '',
            'from db_models.base_model import Base'
        ]

    if (
        args.dimensions and
        any(args.dimensions.get(key).get('type') == 'str' for key in args.dimensions)
    ):
        imports.append('from settings.db import MAX_STRING_LENGTH')

    return imports


def populate_alembic_env_with_db_model(args: argparse.Namespace) -> None:
    """Inserts the db_model import into the alembic env.py file.

    Args:
        args - An object containing attributes parsed out of the command line.
    """
    prefix = 'from db_models.dim_' if args.table_type == 'dim' else 'from db_models.fct_'
    line_to_add = (
        f'from db_models.{args.table_type}_{args.plural_service_name} import '
        f'{args.table_type.capitalize()}{args.plural_schema_name}\n'
    )
    os.chdir('./chalicelib/alembic')
    with open('env.py', 'r') as file:
        lines = file.readlines()

    insert_line_in_alph_order_by_prefix(lines=lines, prefix=prefix, line_to_add=line_to_add)

    with open('env.py', 'w') as file:
        lines = ''.join(lines)
        file.write(lines)
