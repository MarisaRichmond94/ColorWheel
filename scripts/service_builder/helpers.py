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
    foreign_dims_map = {}
    foreign_dims.sort()
    for foreign_dim in foreign_dims:
        split_foreign_dims = foreign_dim.split(',')
        foreign_dims_map[split_foreign_dims[1]] = {
            'plural': split_foreign_dims[0],
            'singular': split_foreign_dims[1],
            'plural_schema': convert_snake_to_camel(split_foreign_dims[0]),
            'singular_schema': convert_snake_to_camel(split_foreign_dims[1])
        }
    return foreign_dims_map


def format_dimensions(dimensions: list) -> None:
    """Formats the dimensions list.

    Args:
        dimensions: A list of dimensions to use for file generation.
    """
    dimensions_map = {}
    dimensions.sort()
    for dimension in dimensions:
        values = dimension.split(',')
        dimensions_map[values[0]] = {
            'key': values[0],
            'sqlalchemy_type': values[1],
            'type': values[2],
            'is_required': True if values[3] == 'True' else False,
            'is_unique': True if values[4] == 'True' else False,
        }
    return dimensions_map


def format_method_args(args: argparse.Namespace) -> None:
    """Formats the method_args list.

    Args:
        args: An object containing attributes parsed out of the command line.
    """
    method_args_map = {}
    for method_args in args.method_args:
        method_args = method_args.split(',')
        arguments = method_args[1:]
        arg_maps = []
        for arg_index, arg in enumerate(arguments):
            if arg == 'skip':
                arg_maps.append(arg)
            else:
                match = get_matching_dimension_info(
                    args=args,
                    key=arg
                )
                arg_maps.append({
                    'key': arguments[arg_index],
                    'type': match.get('type') or 'UUIDType',
                    'sqlalchemy_type': match.get('sqlalchemy_type') or 'UUID'
                })

        method_args_map[method_args[0].upper()] = arg_maps
    return method_args_map


def get_matching_dimension_info(args: argparse.Namespace, key: str) -> dict:
    """Gets the matching dimension for a key if one exists.

    Args:
        args: An object containing attributes parsed out of the command line.
        key: The key of the dimension.

    Returns:
        The dimension matching the given key else None.
    """
    if args.dimensions:
        if args.dimensions.get(key):
            return args.dimensions.get(key)
    if args.foreign_dims and args.table_type == 'fct':
        if args.foreign_dims.get(key):
            return args.foreign_dims.get(key)
    return None
