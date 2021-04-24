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
            "Example = content_items,content_item. Notice that you do not need to include dim or "
            "id in the name. You should just give the plural/singular service name. For the best "
            "results, add these foreign dimensions in alphabetical order."
        )
    )
    parser.add_argument(
        '--dimensions',
        required=False,
        nargs='+',
        help=(
            "A list of values representing table dimensions as strings with values separated "
            "by commas (e.g. name,String,str,True,True order_index,Integer,int,False,False). Note "
            "that dimensions are explicitly different than foreign-dims, which will always be "
            "UUIDs. The order goes: "
            "(field_name),(sql type),(data type),(required/not null),(unique)."
        )
    )
    parser.add_argument(
        '--method-args',
        required=False,
        nargs='+',
        help=(
            "These can only be specified for GET, PATCH, and DELETE and should be formatted as "
            "a list of comma separated strings indicating which methods take what arguments in"
            "(e.g. patch,name,order_index get,name). Everything after the method is considered "
            "arguments and should match up with dimensions or foreign dims (if it's a fct table) "
            "meaning if I have a function that needs to take in a content_item_id and an "
            "order_index, my result would be patch,content_item,order_index. For a foreign-dim, "
            "you should use the singular version passed in; don't worry about the dim or id part."
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
        help='Generate all methods. Overrides any method options.'
    )
    parser.add_argument(
        '--audit',
        action='store_true',
        help="Determines whether or not to generate an audit table for the new table."
    )

    args = parser.parse_args()
    if args.all:
        args.methods = VALID_METHODS
    if args.audit:
        args.audit = True
    args.singular_schema_name = convert_snake_to_camel(args.singular_service_name)
    args.plural_schema_name = convert_snake_to_camel(args.plural_service_name)
    args.singular_param_type = ' '.join(args.singular_service_name.split('-'))
    args.plural_param_type = ' '.join(args.plural_service_name.split('-'))
    args.route = args.plural_service_name.replace("_", "-")
    args.valid_api_schema_methods = 'POST GET PATCH DELETE'
    if args.foreign_dims and args.table_type == 'fct':
        args.foreign_dims = format_foreign_dims(foreign_dims=args.foreign_dims)
    if args.dimensions:
        args.dimensions = format_dimensions(dimensions=args.dimensions)
    if args.method_args:
        args.method_args = format_method_args(args=args)

    return args
