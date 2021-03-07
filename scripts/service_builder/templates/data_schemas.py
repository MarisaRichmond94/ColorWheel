def set_data_schema_constants(arg_dict: dict) -> None:
    """Sets global constants needed to generate templates.

    Args:
        arg_dict: Dict containing constant values.
    """
    global DATA_TYPE
    DATA_TYPE = arg_dict.get('data_type', '')
    global SCHEMA_NAME
    SCHEMA_NAME = arg_dict.get('schema_name', '')
    global SERVICE_NAME
    SERVICE_NAME = arg_dict.get('service_name', '')
    global SINGULAR_PARAM_TYPE
    SINGULAR_PARAM_TYPE = arg_dict.get('singular_param_type', '')
    global TABLE_TYPE
    TABLE_TYPE = arg_dict.get('table_type', '')


def generate_data_schema_file() -> str:
    """Generates a base string for a basic data_schema file.

    Returns:
        A string populated with the given service name.
    """
    return (
        (
            f'"""Data schemas for the {SERVICE_NAME} service."""\n'
            "from marshmallow import fields, Schema, EXCLUDE\n"
            "\n"
            "\n"
            f"class {SCHEMA_NAME}Schema(Schema):\n"\
            f'    """Base data schema for a {SINGULAR_PARAM_TYPE}."""\n'
            "    id = fields.UUID(required=True)\n"
            "    # add any attributes\n"
            "\n"
            "    class Meta:\n"
            "        ordered = True\n"
            "        unknown = EXCLUDE\n"
            "\n"
            "\n"
            f"class Populated{SCHEMA_NAME}Schema(Schema):\n"
            f'    """Populated data schema for a {SINGULAR_PARAM_TYPE}."""\n'
            "    id = fields.UUID(required=True)\n"
            "    # add any attributes\n"
            "\n"
            "    class Meta:\n"
            "        ordered = True\n"
            "        unknown = EXCLUDE\n"
            "\n"
        ) if TABLE_TYPE == 'fct'
        else (
            f'"""Data schemas for the {SERVICE_NAME} service."""\n'
            "from marshmallow import fields, Schema, EXCLUDE\n"
            "\n"
            "\n"
            f"class {SCHEMA_NAME}Schema(Schema):\n"
            f'    """Base data schema for a {SINGULAR_PARAM_TYPE}."""\n'
            "    id = fields.UUID(required=True)\n"
            "    # add any attributes\n"
            "\n"
            "    class Meta:\n"
            "        ordered = True\n"
            "        unknown = EXCLUDE\n"
            "\n"
        )
    )
