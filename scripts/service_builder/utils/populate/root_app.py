"""Populate root app util functions for the service builder script."""
import argparse
import os

from utils.common import insert_line_in_alph_order_by_prefix


def populate_root_app_with_new_api_routes(args: argparse.Namespace) -> None:
    """Populates routes in the root app.py file.

    Args:
        args - An object containing attributes parsed out of the command line.
    """
    os.chdir('../..')

    import_to_add = (
        f'from restful_services.{args.plural_service_name}.api_layer.api import api as '
        f'{args.plural_service_name}_api\n'
    )
    registration_to_add = f'app.register_blueprint({args.plural_service_name}_api)\n'
    routes_to_add = (
        [
            f'@app.route("/{args.route}", methods=["OPTIONS"])\n',
            f'@app.route("/{args.route}/{{{args.singular_service_name}_id}}", methods=["OPTIONS"])\n'
        ] if any(method in ['GET_BY_ID', 'PATCH', 'DELETE_BY_ID'] for method in args.methods)
        else [f'@app.route("/{args.route}", methods=["OPTIONS"])\n']
    )

    with open('app.py', 'r') as file:
        lines = file.readlines()

    insert_line_in_alph_order_by_prefix(lines, 'from restful_services.', import_to_add)
    insert_line_in_alph_order_by_prefix(lines, 'app.register_blueprint(', registration_to_add)
    insert_line_in_alph_order_by_prefix(lines, '@app.route("/', lines_to_add=routes_to_add)

    with open('app.py', 'w') as file:
        lines = ''.join(lines)
        file.write(lines)

    os.chdir('chalicelib/restful_services')
