"""Format method args util functions for the service builder script."""
import argparse


def format_method_args(args: argparse.Namespace) -> None:
    """Formats the method_args list.

    Args:
        args: An object containing attributes parsed out of the command line.

    Returns:
        A map of method names to method args.
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
                    'sqlalchemy_type': match.get('sqlalchemy_type') or 'UUID',
                    'table_type': match.get('table_type')
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
