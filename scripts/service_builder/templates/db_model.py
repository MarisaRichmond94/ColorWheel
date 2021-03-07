def set_db_model_constants(arg_dict: dict) -> None:
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
    global TABLE_TYPE
    TABLE_TYPE = arg_dict.get('table_type', '')


def generate_db_model_file() -> str:
    """Generates a base string for a basic db_model file.

    Returns:
        A string populated with the given service name.
    """
    db_model_file = f'"""The database model for the {TABLE_TYPE}_{SERVICE_NAME} table."""\n'
    db_model_file += (
      "from sqlalchemy import Column\n" if TABLE_TYPE == 'fct'
      else (
          "from sqlalchemy import Column, ForeignKey\n"
          "from sqlalchemy.orm import relationship\n"
          "from sqlalchemy.dialects.postgresql import UUID\n"
      )
    )
    db_model_file += "from db_models.base_model import Base\n"
    db_model_file += "# import dimensions here\n" if TABLE_TYPE == 'fct' else ''
    db_model_file += (
        "\n"
        "\n"
    )
    db_model_file += "# wrap dimensions here (e.g. @DimType.dimension)\n" if TABLE_TYPE == 'fct' else ''
    db_model_file += (
        f"class {TABLE_TYPE.capitalize()}{SCHEMA_NAME}(Base):\n"
        f'    """SQLAlchemy object for the {TABLE_TYPE}_{SERVICE_NAME} table."""\n'
        f'    __tablename__ = "{TABLE_TYPE}_{SERVICE_NAME}"\n'
        "\n"
    )
    db_model_file += '' if TABLE_TYPE == 'fct' else (
        "@classmethod\n"
        "def dimension(cls, target):\n"
        f'    """Class for creating a relationship to the {TABLE_TYPE}_{SERVICE_NAME} table."""\n'
        f'    target.{TABLE_TYPE}_{DATA_TYPE}_id = Column(\n'
        f'        "{TABLE_TYPE}_{DATA_TYPE}_id",\n'
        "        UUID(as_uuid=True),\n"
        f"        ForeignKey({TABLE_TYPE.capitalize()}{SCHEMA_NAME}.id),\n"
        "        nullable=False,\n"
        "    )\n"
        f'    target.{TABLE_TYPE}_{DATA_TYPE} = relationship(cls)\n'
        "    return target\n"
        "\n"
    )
    return db_model_file
