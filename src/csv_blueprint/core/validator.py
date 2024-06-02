"""Rules validator."""

import sys
from colorama import init, Fore
import csv
from itertools import tee
from pathlib import Path

import yaml
from tabulate import tabulate

from csv_blueprint.config import ValidationConfig
from csv_blueprint.core import get_rule
import itertools

try:
    from yaml import CDumper as Dumper  # noqa: F401
    from yaml import CLoader as Loader
except ImportError:
    pass


init()


class Validator:
    """CSV Blueprint Validator class."""

    def __init__(self, config: ValidationConfig) -> None:
        self.config = config

    @classmethod
    def _loadp(cls) -> list:
        """Test method."""
        return [
            {
                "name": "maverick_id",
                "description": "Unique identifier for Maverick",
                "example": "E83AD34C-66DE-41A2-8B4C-C8998A852B98",
                "rules": {
                    "not_empty": False,
                    "is_trimmed": True,
                    "is_uppercase": True,
                    "is_uuid": True,
                },
            },
            {
                "name": "geopath_id",
                "description": "GeoPath ID typically 8 digits",
                "example": "14715555",
                "rules": {
                    "not_empty": True,
                    "is_trimmed": True,
                    "is_int": True,
                    "num_min": 0,
                },
            },
            {
                "name": "cycle_type",
                "description": "The cycle type",
                "example": "1-week",
                "rules": {
                    "not_empty": True,
                    "allow_values": ["1-week", "1-month", "1-year"],
                    "is_int": True,
                    "num_min": 0,
                },
            },
        ]

    @classmethod
    def from_yaml(cls, schema_path: str):  # noqa: ANN206
        with Path(schema_path).open() as stream:
            config = yaml.load(stream=stream, Loader=Loader)  # noqa: S506
            # obj = Validator._loadp() # noqa: ERA001
            return cls(config=config)

    def _process(self, reader, column_config):
        name = column_config.get("name")
        result = []
        for counter, row in enumerate(reader, 1):
            val = row[name]
            for k, v in column_config.get("rules").items():
                rule = get_rule(k, v)
                ok = rule(val)
                if not ok:
                    result.append(
                        {
                            "rule": rule.__class__.__name__,
                            "column": name,
                            "value": val if val else "<empty>",
                            "line": counter,
                        }
                    )
        return result

    def validate(self, csv_path: str):
        result = []
        with Path(csv_path).open("r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            column_configs = self.config.get("columns")
            readers = tee(reader, len(column_configs))

            for reader_conf in zip(readers, column_configs):
                r = reader_conf[0]
                c = reader_conf[1]
                result.extend(self._process(r, c))

            if result:
                print(Fore.RED, len(result), "issues found.")
                counter = itertools.count(start=1)
                print(
                    tabulate(
                        result, headers="keys", tablefmt="github", showindex=counter
                    )
                )
                sys.exit(1)
            else:
                print(Fore.GREEN, "All clear.")
