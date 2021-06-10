"""Format dimensions util functions for the service builder script."""


def format_dimensions(dimensions: list) -> None:
    """Formats the dimensions list.

    Args:
        dimensions: A list of dimensions to use for file generation.
    """
    dimensions_map = {}
    dimensions.sort()
    for dimension in dimensions:
        values = dimension.split(',')
        dimensions_map[values[0]] = {
            'key': values[0],
            'sqlalchemy_type': values[1],
            'type': values[2],
            'is_required': True if values[3] == 'True' else False,
            'is_unique': True if values[4] == 'True' else False,
        }
    return dimensions_map
