"""CSV Blueprint Core module."""

import importlib


def import_string(dotted_path: str):
    """Import a dotted path and return an instance of the class referenced."""
    try:
        module_name, class_name = dotted_path.rsplit(".", 1)
    except ValueError as err:
        msg = f"{dotted_path} improperly formatted dotted path"
        raise ImportError(msg) from err

    module = importlib.import_module(module_name)

    return getattr(module, class_name)


def get_rule(class_name, *args):
    """Instantiate a rule class."""
    module = importlib.import_module("csv_blueprint.rules")
    klass = getattr(module, class_name)

    return klass(*args)
