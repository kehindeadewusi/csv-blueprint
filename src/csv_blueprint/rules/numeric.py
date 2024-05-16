"""CSV Blueprint in-built numeric rules."""

from __future__ import annotations


class is_int:
    """Checks if the current value is an integer."""

    def __init__(self, b: bool) -> None:
        self.b = b

    def __call__(self, value: str) -> bool:
        try:
            new_value = int(value)
            result = len(str(new_value)) == len(str(value))
        except ValueError:
            result = False

        if self.b:
            return result

        return not result


class is_float:
    """Checks if the current value is a floating point type."""

    def __init__(self, b: bool) -> None:
        self.b = b

    def __call__(self, value: str) -> bool:
        try:
            value = float(value)
            result = isinstance(value, float)
        except ValueError:
            result = False

        if self.b:
            return result

        return not result


class num_min:
    """Assert the value is greater than the minimum specified."""

    def __init__(self, xmin: float) -> None:
        self.min = xmin

    def __call__(self, val) -> bool:
        if not val:
            return False

        try:
            val = float(val)
        except ValueError:
            return False

        return val >= float(self.min)


class num_max:
    """Asserts the value is less than or equal to the maximum specified.

    >> num_max: 9.0                      # x <= 9.0
    """

    def __init__(self, xmax: float) -> None:
        self.max = xmax

    def __call__(self, val) -> bool:
        if not val:
            return False

        try:
            val = float(val)
        except ValueError:
            return False

        return val <= float(self.max)


class num_greater:
    """Asserts that the value is greater than the specified value.

    num_greater: 2.0                  # x >  2.0
    """

    def __init__(self, in_value: float) -> None:
        self.in_value = in_value

    def __call__(self, val) -> bool:
        if not val:
            return False

        try:
            val = float(val)
        except ValueError:
            return False

        return val > float(self.in_value)


class num_less:
    """Asserts that the value is less than the specified value.

    >>> num_less: 8.0  # x <  8.0
    """

    def __init__(self, in_value: float) -> None:
        self.in_value = in_value

    def __call__(self, val) -> bool:
        if not val:
            return False

        try:
            val = float(val)
        except ValueError:
            return False

        return val < float(self.in_value)


class num_not:
    """num_not: 5.0                      # x != 5.0."""

    def __init__(self, in_value: float) -> None:
        self.in_value = in_value

    def __call__(self, val) -> bool:
        if not val:
            return False

        try:
            val = float(val)
        except ValueError:
            return False

        return val != float(self.in_value)


class num:
    """Asserts that the in_value is same as the value.

    >>> num: 7.0  # x == 7.0
    """

    def __init__(self, in_value: float) -> None:
        self.in_value = in_value

    def __call__(self, val) -> bool:
        if not val:
            return False

        try:
            val = float(val)
        except ValueError:
            return False

        return val == float(self.in_value)


# precision and scale function
def _get_precision_and_scale(f: float) -> tuple[int, int]:
    f = abs(f)
    sf = str(f)  # works ok on Python
    a, b = sf.split(".")
    return len(a) + len(b), len(b)


class scale_min:
    """Asserts input value is at least the provided scale.

    >>> scale_min: 1  # scale(x) >= 1
    """

    def __init__(self, in_value: int) -> None:
        self.in_value = in_value

    def __call__(self, val) -> bool:
        if not val:
            return False

        try:
            val = float(val)
        except ValueError:
            return False

        _, scale = _get_precision_and_scale(float(val))
        return scale >= int(self.in_value)


class scale_max:
    """9                  # x <= 9."""

    def __init__(self, in_value: int) -> None:
        self.in_value = in_value

    def __call__(self, val) -> bool:
        if not val:
            return False

        try:
            val = float(val)
        except ValueError:
            return False

        _, scale = _get_precision_and_scale(float(val))

        return scale <= int(self.in_value)


class scale_greater:
    """2              # x >  2."""

    def __init__(self, in_value: int) -> None:
        self.in_value = in_value

    def __call__(self, val) -> bool:
        if not val:
            return False

        try:
            val = float(val)
        except ValueError:
            return False

        _, scale = _get_precision_and_scale(float(val))

        return scale > int(self.in_value)


class scale_less:
    """8                 # x <  8."""

    def __init__(self, in_value: int) -> None:
        self.in_value = in_value

    def __call__(self, val) -> bool:
        if not val:
            return False

        try:
            val = float(val)
        except ValueError:
            return False

        _, scale = _get_precision_and_scale(float(val))

        return scale < int(self.in_value)


class scale_not:
    """0                  # x != 0."""

    def __init__(self, in_value: int) -> None:
        self.in_value = in_value

    def __call__(self, val) -> bool:
        if not val:
            return False
        try:
            val = float(val)
        except ValueError:
            return False

        _, scale = _get_precision_and_scale(float(val))

        return scale != int(self.in_value)


class scale:
    """7                      # x == 7."""

    def __init__(self, in_value: int) -> None:
        self.in_value = in_value

    def __call__(self, val) -> bool:
        if not val:
            return False

        try:
            val = float(val)
        except ValueError:
            return False

        _, scale = _get_precision_and_scale(float(val))

        return scale == int(self.in_value)


# precision
class precision_min:
    """Asserts input value is at least the provided scale.

    >>> precision_min: 1  # precision(x) >= 1
    The precision of 123.4562 is 7
    """

    def __init__(self, in_value: int) -> None:
        self.in_value = in_value

    def __call__(self, val) -> bool:
        if not val:
            return False

        try:
            val = float(val)
        except ValueError:
            return False

        precision, _ = _get_precision_and_scale(float(val))
        return precision >= int(self.in_value)


class precision_max:
    """9                  # x <= 9.

    The precision of 123.4562 is 7
    """

    def __init__(self, in_value: int) -> None:
        self.in_value = in_value

    def __call__(self, val) -> bool:
        if not val:
            return False

        try:
            val = float(val)
        except ValueError:
            return False

        precision, _ = _get_precision_and_scale(float(val))

        return precision <= int(self.in_value)


class precision_greater:
    """2              # x >  2.

    The precision of 123.4562 is 7
    """

    def __init__(self, in_value: int) -> None:
        self.in_value = in_value

    def __call__(self, val) -> bool:
        if not val:
            return False

        try:
            val = float(val)
        except ValueError:
            return False

        precision, _ = _get_precision_and_scale(val)

        return precision > int(self.in_value)


class precision_less:
    """8                 # x <  8.

    The precision of 123.4562 is 7
    """

    def __init__(self, in_value: int) -> None:
        self.in_value = in_value

    def __call__(self, val) -> bool:
        if not val:
            return False

        try:
            val = float(val)
        except ValueError:
            return False

        precision, _ = _get_precision_and_scale(float(val))

        return precision < int(self.in_value)


class precision_not:
    """0                  # x != 0.

    The precision of 123.4562 is 7
    """

    def __init__(self, in_value: int) -> None:
        self.in_value = in_value

    def __call__(self, val) -> bool:
        if not val:
            return False

        try:
            val = float(val)
        except ValueError:
            return False

        precision, _ = _get_precision_and_scale(float(val))

        return precision != int(self.in_value)


class precision:
    """7                      # x == 7.

    The precision of 123.4562 is 7
    """

    def __init__(self, in_value: int) -> None:
        self.in_value = in_value

    def __call__(self, val) -> bool:
        if not val:
            return False

        try:
            val = float(val)
        except ValueError:
            return False

        precision, _ = _get_precision_and_scale(val)

        return precision == int(self.in_value)
