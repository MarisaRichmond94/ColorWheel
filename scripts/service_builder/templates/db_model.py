import settings as args


def generate_db_model_file() -> str:
    """Generates a base string for a basic db_model file.

    Returns:
        A string populated with the given service name.
    """
    db_model_file = (
        f'"""The database model for the {args.TABLE_TYPE}_{args.SERVICE_NAME} '
        'table."""\n'
    )
    db_model_file += (
        "from sqlalchemy import Column\n" if args.TABLE_TYPE == 'fct'
        else (
            "from sqlalchemy import Column, ForeignKey\n"
            "from sqlalchemy.orm import relationship\n"
            "from sqlalchemy.dialects.postgresql import UUID\n"
        )
    )
    db_model_file += "from db_models.base_model import Base\n"
    db_model_file += "# import dimensions here\n" if args.TABLE_TYPE == 'fct' else ''
    db_model_file += (
        "\n"
        "\n"
    )
    db_model_file += (
        "# wrap dimensions here (e.g. @DimType.dimension)\n" if args.TABLE_TYPE == 'fct' else ''
    )
    db_model_file += (
        f"class {args.TABLE_TYPE.capitalize()}{args.SCHEMA_NAME}(Base):\n"
        f'    """SQLAlchemy object for the {args.TABLE_TYPE}_{args.SERVICE_NAME} table."""\n'
        f'    __tablename__ = "{args.TABLE_TYPE}_{args.SERVICE_NAME}"\n'
        "    # list any table fields here\n"
        "\n"
    )
    db_model_file += '' if args.TABLE_TYPE == 'fct' else (
        "@classmethod\n"
        "def dimension(cls, target):\n"
        f'    """Class for creating a relationship to the {args.TABLE_TYPE}_{args.SERVICE_NAME} '
        'table."""\n'
        f'    target.{args.TABLE_TYPE}_{args.DATA_TYPE}_id = Column(\n'
        f'        "{args.TABLE_TYPE}_{args.DATA_TYPE}_id",\n'
        "        UUID(as_uuid=True),\n"
        f"        ForeignKey({args.TABLE_TYPE.capitalize()}{args.SCHEMA_NAME}.id),\n"
        "        nullable=False,\n"
        "    )\n"
        f'    target.{args.TABLE_TYPE}_{args.DATA_TYPE} = relationship(cls)\n'
        "    return target\n"
        "\n"
    )
    return db_model_file
