import os

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
    with open(os.path.join(os.getcwd(), '__init__.py'), 'w') as init:
        pass
