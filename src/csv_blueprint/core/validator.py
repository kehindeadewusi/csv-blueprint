"""Rules validator."""

import csv
from itertools import tee
from pathlib import Path

from tabulate import tabulate

from csv_blueprint.config import ValidationConfig
from csv_blueprint.core import get_rule

try:
    from yaml import CDumper as Dumper  # noqa: F401
    from yaml import CLoader as Loader  # noqa: F401
except ImportError:
    pass


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
    def from_yaml(cls, schema_path: str):  # noqa: ARG003, ANN206
        # obj = load(schema, Loader=Loader)  # noqa: ERA001
        obj = Validator._loadp()
        return cls(config=obj)

    def _process(self, reader, config):
        header = config["name"]
        result = []
        for row in reader:
            val = row[header]
            for k, v in config.get("rules").items():
                rule = get_rule(k, v)
                ok = rule(val)
                if not ok:
                    result.append(
                        {
                            "rule": rule,
                            "value": val,
                        }
                    )
        return result

    def validate(self, csv_path: str):
        with Path(csv_path).open("r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            readers = tee(reader, len(self.config))

            for reader_conf in zip(readers, self.config):
                r = reader_conf[0]
                c = reader_conf[1]
                result = self._process(r, c)
                print(tabulate(result, tablefmt="github"))  # noqa: T201
