"""Setup functionality for the service builder script."""
import argparse

from utils.common import convert_snake_to_camel
from utils.format.dimensions import format_dimensions
from utils.format.foreign_dims import format_foreign_dims
from utils.format.method_args import format_method_args
from utils.format.method_permissions import format_method_permissions

VALID_METHODS = ["POST", "GET", "GET_BY_ID", "PATCH", "DELETE", "DELETE_BY_ID"]


def parse_command_line_options() -> argparse.Namespace:
    """Parses out command line options in order to build a dictionary.

    Returns:
        An object containing attributes parsed out of the command line.
    """
    parser = argparse.ArgumentParser(
        description=(
            "Service Builder is a script that has the potential to generate and test a "
            "fully functional RESTful service and table. ¯\_(ツ)_/¯"
        ),
        epilog="Happy coding! ヘ( ^o^)ノ＼(^_^ )"
    )
    parser.add_argument(
        "-p", "--plural-service-name",
        required=True,
        help=(
            "(Required) The plural form of the new service to create. This should be given in "
            "snake case. EXAMPLE: form_data_types"
        )
    )
    parser.add_argument(
        "-s", "--singular-service-name",
        required=True,
        help=(
            "(Required) The singular form of the new service to create. This should be given in "
            "snake case. EXAMPLE: form_data_type"
        )
    )
    parser.add_argument(
        "-t", "--table-type",
        choices=["dim", "fct"],
        required=True,
        help="(Required) The type of table to create for this service. Choices are: %(choices)s."
    )
    parser.add_argument(
        "-m", "--methods",
        choices=VALID_METHODS,
        nargs="+",
        help="(Required) The method(s) to generate for this service.  Choices are: %(choices)s."
    )
    parser.add_argument(
        "-fdims", "--foreign-dims",
        required=False,
        nargs="+",
        help=(
            "(Optional) A list of foreign dimensions to attach to a model and data schema. "
            "These should be given in snake case, comma separated format providing the plural "
            "form, the singular form, and the table type for that foreign dimension. "
            "EXAMPLE: data_types,data_type,dim. NOTE that you do not need to include dim/fct or "
            "id in the name. You should just give the plural/singular service name for that "
            "foreign dimension."
        )
    )
    parser.add_argument(
        "-dims", "--dimensions",
        required=False,
        nargs="+",
        help=(
            "(Optional) A list of values representing table dimensions. These should be given as "
            "comma separated strings. EXAMPLE: name,String,str,True,True "
            "order_index,Integer,int,True,True indicates that there are two dimensions (name and "
            "order_index) along with all the necessary information, including the sql type, the "
            "python data type, whether or not the dimension is required to be defined and whether "
            "or not it has a unique constraint. NOTE that dimensions are explicitly different "
            "than foreign-dims, which will always be UUIDs."
        )
    )
    parser.add_argument(
        "-margs", "--method-args",
        required=False,
        nargs="+",
        help=(
            "(Optional) A list of arguments needed for a method. These can only be specified for "
            "GET, PATCH, and DELETE and should be formatted as comma separated strings, each "
            "indicating the method followed by any arguments the method takes in. EXAMPLE: "
            "patch,name,order_index get,name. Any arguments need to match up with either a given "
            "dimension or foreign dimension. For a foreign dimension, use the singular service "
            "form (e.g. for dim_content_item_id, use just content_item)."
        )
    )
    parser.add_argument(
        "-mp", "--method-permissions",
        required=False,
        nargs="+",
        help=(
            "(Optional) A list of permissions needed for a method. These should be formatted as a "
            "comma separated strings, each indicating the method followed by any required "
            "permissions. EXAMPLE: patch,edit_user. Notice the lowercase string format is used."
        )
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="(Optional) Generates all methods. This option overrides any method options."
    )
    parser.add_argument(
        "-d", "--dimension",
        action="store_true",
        help="(Optional) Determines whether or not to generate a class dimension for a fct table."
    )
    parser.add_argument(
        "-r", "--relationship",
        action="store_true",
        help="(Optional) Determines whether or not to generate parent and child dimensions for a "
        "database model."
    )
    parser.add_argument(
        "--no-api",
        action="store_true",
        help="(Optional) Determines whether or not to ignore api layer creation and testing."
    )

    args = parser.parse_args()
    if args.all:
        args.methods = VALID_METHODS
    if args.dimension:
        args.dimension = True
    if args.relationship:
        args.relationship = True
    args.generate_api_layer = False if args.no_api else True
    args.singular_schema_name = convert_snake_to_camel(args.singular_service_name)
    args.plural_schema_name = convert_snake_to_camel(args.plural_service_name)
    args.singular_param_type = " ".join(args.singular_service_name.split("-"))
    args.plural_param_type = " ".join(args.plural_service_name.split("-"))
    args.route = args.plural_service_name.replace("_", "-")
    args.valid_api_schema_methods = "POST GET PATCH DELETE"
    if args.foreign_dims and args.table_type == "fct":
        args.foreign_dims = format_foreign_dims(foreign_dims=args.foreign_dims)
    if args.dimensions:
        args.dimensions = format_dimensions(dimensions=args.dimensions)
    if args.method_args:
        args.method_args = format_method_args(args=args)
    if args.method_permissions:
        args.method_permissions = format_method_permissions(args=args)

    return args
