"""Format foreign dimensions util functions for the service builder script."""
from utils.common import convert_snake_to_camel


def format_foreign_dims(foreign_dims: list) -> None:
    """Formats the foreign_dims list.

    Args:
        foreign_dims: A list of foreign dimensions to use for file generation.
    """
    foreign_dims_map = {}
    foreign_dims.sort()
    for foreign_dim in foreign_dims:
        split_foreign_dims = foreign_dim.split(',')
        foreign_dims_map[split_foreign_dims[1]] = {
            'plural': split_foreign_dims[0],
            'singular': split_foreign_dims[1],
            'plural_schema': convert_snake_to_camel(split_foreign_dims[0]),
            'singular_schema': convert_snake_to_camel(split_foreign_dims[1]),
            'table_type': split_foreign_dims[2]
        }
    return foreign_dims_map
