"""Format method permissions util functions for the service builder script."""
import argparse


def format_method_permissions(args: argparse.Namespace) -> dict:
    """Formats the method_permissions list.

    Args:
        args: An object containing attributes parsed out of the command line.

    Returns:
        A map of method names to method required permissions.
    """
    method_permissions_map = {}
    for method_permissions in args.method_permissions:
        method_permissions = method_permissions.split(',')
        required_permissions_string = ''
        for permission in sorted(method_permissions[1:]):
            required_permissions_string += f'{permission.upper()}, '
        method_permissions_map[method_permissions[0]] = {
            "required_permissions_lower": sorted(method_permissions[1:]),
            "required_permissions_upper": sorted([x.upper() for x in method_permissions[1:]]),
            "required_permissions_string": required_permissions_string[:len(required_permissions_string) - 2]
        }

    return method_permissions_map
