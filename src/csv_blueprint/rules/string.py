"""CSV Blueprint in-built string rules."""

import re
import uuid


class not_empty:
    """Ensures the current value is not empty or not None."""

    def __init__(self, b: bool) -> None:
        self.b = b

    def __call__(self, value: str) -> bool:
        result = value not in ("", None)

        if self.b:
            return result

        return not result


class exact_value:
    """Ensures the current value is not empty or not Note."""

    def __init__(self, in_value: str) -> None:
        self.in_value = in_value

    def __call__(self, value: str) -> bool:
        return self.in_value == value


class regex:
    """Checks if the current value matches a regex."""

    def __init__(self, regex) -> None:
        self.regex_comp = re.compile(regex)

    def __call__(self, value: str) -> bool:
        result = self.regex_comp.match(value)

        return result is not None and result.group() is not None


class is_trimmed:
    """Ensures there are no leading nor trailing spaces."""

    def __init__(self, b: bool) -> None:
        self.b = b
        self.errors = ()

    def __call__(self, value: str) -> bool:
        result = value == value.strip()
        if self.b:
            return result

        return not result


class is_uppercase:
    """Ensure all CAPS."""

    def __init__(self, b: bool) -> None:
        self.b = b

    def __call__(self, value: str) -> bool:
        result = value == value.upper()
        if self.b:
            return result

        return not result


class is_lowercase:
    """Ensure NO CAPS.

    usage: `is_lowercase: true`
    """

    def __init__(self, b: bool) -> None:
        self.b = b

    def __call__(self, value: str) -> bool:
        result = value == value.lower()
        if self.b:
            return result

        return not result


class is_uuid:
    """Ensures a valid UUID string."""

    def __init__(self, b: bool) -> None:
        self.b = b

    def __call__(self, value: str) -> bool:
        try:
            uuid.UUID(str(value))
            result = True
        except ValueError:
            result = False

        if self.b:
            return result

        return not result


class length_min:
    """Ensure that the input is a minimum length."""

    def __init__(self, in_value: int) -> None:
        self.in_value = in_value

    def __call__(self, value: str) -> bool:
        return len(value) >= self.in_value


class length_max:
    """Ensure that the input less than or equal to a max value."""

    def __init__(self, in_value: int) -> None:
        self.in_value = in_value

    def __call__(self, value: str) -> bool:
        return len(value) <= self.in_value


class length_greater:
    """Assert length of input is greater than value.

    # x >  2
    """

    def __init__(self, in_value: int) -> None:
        self.in_value = in_value

    def __call__(self, value: str) -> bool:
        return len(value) > self.in_value


class length_less:
    """Assert length of input is less than value.

    # x <  8
    """

    def __init__(self, in_value: int) -> None:
        self.in_value = in_value

    def __call__(self, value: str) -> bool:
        return len(value) < self.in_value


class length_not:
    """Assert length of input is not value.

    length_not: 0 # x != 0
    """

    def __init__(self, in_value: int) -> None:
        self.in_value = in_value

    def __call__(self, value: str) -> bool:
        return len(value) != self.in_value


class length:
    """Assert length of input is exactly value.

    # x == 7
    """

    def __init__(self, in_value: int) -> None:
        self.in_value = in_value

    def __call__(self, value: str) -> bool:
        return len(value) == self.in_value


class is_sentence:
    """# Sentence with at least one space. Example: "Hello world!"."""

    def __init__(self, b: int) -> None:
        self.b = b

    def __call__(self, value: str) -> bool:
        value = str(value)
        result = len(value.split(" ")) > 1

        if self.b:
            return result

        return not result
