"""CSV Blueprint CLI module."""

import multiprocessing

import click

from csv_blueprint.core.validator import Validator

multiprocessing.set_start_method("spawn")


@click.command(short_help="Validate a CSV file against a schema.")
@click.option("--csv", "-c", required=True, help="Path to the csv file.")
@click.option("--schema", "-s", required=True, help="Path to the YAML schema.")
@click.option(
    "--ansi",
    default="ansi",
    type=click.Choice(["ansi"], case_sensitive=False),
)
def validate_csv(csv: str, schema: str, ansi: str):  # noqa: ARG001
    """Validate a CSV file against a YAML schema."""
    validator = Validator.from_yaml(schema)

    return validator.validate(csv)


def debug_schema(schema):  # noqa: ARG001
    """Debug a schema."""


@click.command(short_help="Creates a schema ffrom a CSV file.")
@click.option("--csv", "-c", required=True, help="Path to the csv file.")
def create_schema(csv: str):  # noqa: ARG001
    """Generate a schema from a CSV file."""


def schema():
    """Create schema command."""
    try:
        create_schema()
    except SystemExit as err:
        if err.code:
            raise


def main():
    """Cli entry function."""
    try:
        validate_csv()
    except SystemExit as err:
        # re-raise unless main() finished without an error
        if err.code:
            raise
