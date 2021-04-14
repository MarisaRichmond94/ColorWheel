"""Setup functionality for the service builder script."""
import argparse

from helpers import (
    convert_snake_to_camel,
    format_dimensions,
    format_foreign_dims,
    format_method_args
)

VALID_METHODS = ['POST', 'GET', 'GET_BY_ID', 'PATCH', 'DELETE', 'DELETE_BY_ID']


def parse_command_line_options() -> argparse.Namespace:
    """Parses out command line options in order to build a dictionary.

    Returns:
        An object containing attributes parsed out of the command line.
    """
    parser = argparse.ArgumentParser(
        description="Script to generate most of the code needed for writing a service."
    )
    parser.add_argument(
        '--plural-service-name',
        required=True,
        help='The name of the service to create (plural).  Should be snake case.'
    )
    parser.add_argument(
        '--singular-service-name',
        required=True,
        help='The name of the service to create (singular). Should be snake case.'
    )
    parser.add_argument(
        '--table-type',
        choices=['dim', 'fct'],
        required=True,
        help="The type of table to use for this service. Choices are: %(choices)s"
    )
    parser.add_argument(
        '--foreign-dims',
        required=False,
        nargs='+',
        help=(
            "A list of foreign dimensions to attach to a model and data schema"
            "(fct tables only and should be in snake case comma separating plural,singular)."
            "Example = content_items,content_item"
        )
    )
    parser.add_argument(
        '--dimensions',
        required=False,
        nargs='+',
        help=(
            "A list of values representing table dimensions as single strings with values separated"
            "by commas (e.g. name,String,str,true order_index,Integer,int,false)."
        )
    )
    parser.add_argument(
        '--method-args',
        required=False,
        nargs='+',
        help=(
            "A list of comma separated strings indicating which methods take what arguments in"
            "(e.g. patch,name,order_index get,name)"
        )
    )
    parser.add_argument(
        '--methods',
        choices=VALID_METHODS,
        nargs='+',
        help="The methods to generate for this service.  Choices are: %(choices)s"
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Generate all methods.  Overrides any method options.'
    )

    args = parser.parse_args()
    if args.all:
        args.methods = VALID_METHODS
    args.singular_schema_name = convert_snake_to_camel(args.singular_service_name)
    args.plural_schema_name = convert_snake_to_camel(args.plural_service_name)
    args.singular_param_type = ' '.join(args.singular_service_name.split('-'))
    args.plural_param_type = ' '.join(args.plural_service_name.split('-'))
    args.route = args.plural_service_name.replace("_", "-")
    args.valid_api_schema_methods = 'POST GET PATCH DELETE'
    if args.foreign_dims and args.table_type == 'fct':
        format_foreign_dims(foreign_dims=args.foreign_dims)
    if args.dimensions:
        format_dimensions(dimensions=args.dimensions)
    if args.method_args:
        format_method_args(args=args)

    return args
