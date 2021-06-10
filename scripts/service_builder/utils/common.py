"""Common util functions for the service builder script."""
import os
from typing import Optional


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


def insert_line_in_alph_order_by_prefix(
    lines: list,
    prefix: str,
    line_to_add: Optional[str] = None,
    lines_to_add: Optional[list] = None
) -> None:
    """Inserts a line into a file in alphabetical order using a given index.

    Args:
        lines: A list of lines from a file.
        prefix: The prefix to search on.
        line_to_add: The desired add to add to the file.
        lines_to_add: A list of lines to add to the file in reverse order.
    """
    if line_to_add and line_to_add not in lines:
        for index, line in enumerate(lines):
            if prefix in line and line_to_add < line:
                lines.insert(index, line_to_add)
                return
        lines.append(line_to_add)
    if lines_to_add and lines_to_add[0] not in lines:
        for index, line in enumerate(lines):
            if prefix in line and lines_to_add[0] < line:
                for line_index, ln_to_add in enumerate(lines_to_add):
                    lines.insert(index + line_index, ln_to_add)
                return
        lines.append(lines_to_add)


def create_directory(path: str) -> None:
    """Creates a directory or file given a path if one does not currently exist

    Args:
        path: path to directory or file

    Returns:
        None
    """
    if not os.path.exists(path):
        os.mkdir(path)
