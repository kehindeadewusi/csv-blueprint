"""CSV Blueprint in-built boolean rules."""


class is_bool:
    """Rule to check if every record in column is a boolean.

    The rule handles Python `True` and `False` correctly, and
    makes a special case for `true` and `false` strings, treating
    them as Python `True` and `False`.
    """

    bool_values = (
        "TRUE",
        "FALSE",
    )

    def __init__(self, b: bool) -> None:
        self.b = str(b).upper() == "TRUE"

    def __call__(self, value: str) -> bool:
        value = str(value).upper()
        if self.b:
            return value in self.bool_values

        return str(value).upper() not in self.bool_values
