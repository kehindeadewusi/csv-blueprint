"""CSV Blueprint in-built boolean rules."""


class is_bool:
    """Rule to check if every record in column is a boolean.

    The rule handles Python `True` and `False` correctly, and
    makes a special case for `true` and `false` strings, treating
    them as Python `True` and `False`.
    """

    true_values = ("True", "true", True, "False", "false", False)

    def __init__(self, b: bool) -> None:
        self.b = b

    def __call__(self, value: str) -> bool:
        if self.b:
            return value in self.true_values

        return value not in self.true_values
