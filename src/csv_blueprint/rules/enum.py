"""CSV Blueprint in-built enumeration rules."""

from __future__ import annotations


class allow_values:
    """Rule to check if every record in column is a boolean.

    The rule handles Python `True` and `False` correctly, and
    makes a special case for `true` and `false` strings, treating
    them as Python `True` and `False`.
    """

    def __init__(self, whilelist: list[str]) -> None:
        """Initialize `allow_values` with a whitelist."""
        self.whilelist = whilelist

    def __call__(self, value: str) -> bool:
        return value in self.whilelist


class not_allow_values:
    """Rule to checks a blacklisted value.

    It fails if the test value matches any
    value in the blacklist.
    """

    def __init__(self, blacklist: list[str]) -> None:
        self.blacklist = blacklist

    def __call__(self, value: str) -> bool:
        return value not in self.blacklist
