"""Helper functions for the service builder script."""
import argparse
import os


def convert_snake_to_camel(snake_string: str) -> str:
    """Converts a string from being snake case to camel case.

    Args:
        snake_string: A snake cased string.

    Returns:
        A camel cased string.
    """
    split_snake_string = snake_string.split('_')
    capitalized_words_list = [item.capitalize() for item in split_snake_string]
    return ''.join(capitalized_words_list)


def generate_init_file() -> None:
    """Creates a blank __init__.py file."""
    with open(os.path.join(os.getcwd(), '__init__.py'), 'w'):
        pass


def format_foreign_dims(foreign_dims: list) -> None:
    """Formats the foreign_dims list.

    Args:
        foreign_dims: A list of foreign dimensions to use for file generation.
    """
    foreign_dims.sort()
    for index, foreign_dim in enumerate(foreign_dims):
        split_foreign_dims = foreign_dim.split(',')
        foreign_dims[index] ={
            'plural': split_foreign_dims[0],
            'singular': split_foreign_dims[1],
            'schema': convert_snake_to_camel(split_foreign_dims[0])
        }


def format_dimensions(dimensions: list) -> None:
    """Formats the dimensions list.

    Args:
        dimensions: A list of dimensions to use for file generation.
    """
    dimensions.sort()
    for index, dimension in enumerate(dimensions):
        values = dimension.split(',')
        dimensions[index] = {
            'key': values[0],
            'sqlalchemy_type': values[1],
            'type': values[2],
            'is_required': values[3]
        }


def format_method_args(args: argparse.Namespace) -> None:
    """Formats the method_args list.

    Args:
        args: An object containing attributes parsed out of the command line.
    """
    for index, method_args in enumerate(args.method_args):
        method_args = method_args.split(',')
        arguments = method_args[1:]
        arg_maps = []
        for arg_index, arg in enumerate(arguments):
            match = get_matching_dimension_info(
                args=args,
                key=arg
            )
            arg_maps.append({
                'key': arguments[arg_index],
                'type': match['type'] or 'UUIDType',
                'sqlalchemy_type': match['sqlalchemy_type'] or 'UUID'
            })
        args.method_args[index] = {
            'method': method_args[0].upper(),
            'args': arg_maps
        }


def get_matching_dimension_info(args: argparse.Namespace, key: str) -> dict:
    """Gets the matching dimension for a key if one exists.

    Args:
        args: An object containing attributes parsed out of the command line.
        key: The key of the dimension.

    Returns:
        The dimension matching the given key else None.
    """
    if args.dimensions:
        for dimension in args.dimensions:
            if dimension['key'] == key:
                return dimension
    if args.foreign_dims and args.table_type == 'fct':
        for foreign_dim in args.foreign_dims:
            if foreign_dim.singular == key:
                return foreign_dim
    return None
