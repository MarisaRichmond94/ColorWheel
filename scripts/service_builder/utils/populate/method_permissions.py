"""Populate method permissions util functions for the service builder script."""
import os
from typing import Optional


def populate_method_permissions(method_permissions: dict) -> None:
    """Populates any method permissions that are missing from the settings.permissions file.

    Args:
        method_permissions: A map of method names to required permissions.
    """
    print('Attempting to create any new required permissions...')
    os.chdir('./settings')

    with open('permissions.py', 'r') as file:
        lines = file.readlines()

    all_permissions = [
        required_permissions
        for method_permissions in method_permissions.values()
        for required_permissions in method_permissions.get("required_permissions_lower")
    ]
    unique_sorted_permissions = sorted(list(set(all_permissions)))
    for permission in unique_sorted_permissions:
        insert_line_in_alph_order(lines, f'{permission.upper()} = "{permission}"\n')

    with open('permissions.py', 'w') as file:
        lines = ''.join(lines)
        file.write(lines)

    os.chdir('..')


def insert_line_in_alph_order(
    lines: list,
    line_to_add: Optional[str] = None
) -> None:
    """Inserts a line into a file in alphabetical order using a given index.

    Args:
        lines: A list of lines from a file.
        line_to_add: The desired add to add to the file.
    """
    if line_to_add and line_to_add not in lines:
        for index, line in enumerate(lines):
            if line_to_add < line:
                lines.insert(index, line_to_add)
                return
        lines.append(line_to_add)
