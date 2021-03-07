from settings import (
    DATA_TYPE,
    SCHEMA_NAME,
    SERVICE_NAME,
    SINGULAR_PARAM_TYPE,
    TABLE_TYPE,
)


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
