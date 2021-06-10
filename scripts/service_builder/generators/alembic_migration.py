"""Generator for the alembic migration."""
import argparse
import os
import re


def generate_alembic_migration_command(args: argparse.Namespace) -> str:
    """Generates an alembic migration command.

    Args:
        args - An object containing attributes parsed out of the command line.

    Returns:
        An alembic migration command with the latest revision id.
    """
    files = os.listdir('versions')
    versions = []
    for file in files:
        pattern = re.compile(r'([0-9]*)_(.*)\.py')
        if match := pattern.match(file):
            versions.append(match.group(1))
    latest_migration_version = sorted(versions, reverse=True)[0]
    new_version = str(int(latest_migration_version) + 1).zfill(len(latest_migration_version))

    return (
        'alembic -c chalicelib/alembic.ini revision --autogenerate -m "create '
        f'{args.plural_service_name} table" --rev-id {new_version}'
    )