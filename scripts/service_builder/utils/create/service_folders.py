"""Create service folders util functions for the service builder script."""
import argparse
import os

from utils.common import create_directory, generate_init_file


def create_restful_service_folders(args: argparse.Namespace) -> None:
    """Creates all of the base-level folders needed for the new service given a valid name.

    Args:
        args - An object containing attributes parsed out of the command line.
    """
    print(f'Generating new service with name {args.plural_service_name}...')
    create_directory(f'./{args.plural_service_name}')
    os.chdir(f'./{args.plural_service_name}')
    generate_init_file()
    if args.generate_api_layer:
        create_directory('./api_layer')
    create_directory('./business_layer')
    create_directory('./data_layer')
    create_directory('./model_layer')