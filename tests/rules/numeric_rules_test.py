"""Numeric rules unit tests."""

from csv_blueprint.rules.numeric import (
    is_float,
    is_int,
    num,
    num_greater,
    num_less,
    num_max,
    num_min,
    num_not,
    precision,
    precision_greater,
    precision_less,
    precision_max,
    precision_min,
    precision_not,
    scale,
    scale_greater,
    scale_less,
    scale_max,
    scale_min,
    scale_not,
)


class TestIsFloat:
    """is_float test cases."""

    def test_ok_is_float(self):
        """Test is_float ok."""
        rule = is_float(b=True)
        assert rule(13.245)

    def test_inverted_is_float(self):
        """Test is_float inverted."""
        rule = is_float(b=False)
        assert not rule(13.245)

    def test_ok_str_is_float(self):
        """Test is_float ok string input."""
        rule = is_float(b=True)
        assert rule("13.245")

    def test_not_ok_is_float(self):
        """Test False not float."""
        rule = is_float(b=True)
        assert not rule("abec")


class TestInInt:
    """is_int test cases."""

    def test_ok_is_int(self):
        """Test is_int ok."""
        rule = is_int(b=True)
        assert rule(12345)

    def test_inverted_is_int(self):
        """Test is_int inverted."""
        rule = is_int(b=False)
        assert not rule(12345)

    def test_ok_str_is_int(self):
        """Test is_int ok string input."""
        rule = is_int(b=True)
        assert rule("12345")

    def test_not_ok_is_int(self):
        """Test is_int bad input."""
        rule = is_int(b=True)
        assert not rule(123.56)
        assert not rule("abc")


class TestNum:
    """num test cases."""

    def test_ok_num(self):
        """Test the expected number."""
        rule = num(123.45)
        assert rule(123.45)

    def test_no_ok_num(self):
        """Test not the expected number."""
        rule = num(123.45)
        assert not rule(123.4)


class TestNumGreater:
    """num_greater test cases."""

    def test_ok_num_greater(self):
        """Test input greater than expected value OK."""
        rule = num_greater(123.45)
        assert rule(124.01)

    def test_not_ok_num_greater(self):
        """Test input failure when less than expected."""
        rule = num_greater(123.45)
        assert not rule(123.0)

    def test_not_ok_equal(self):
        """Test input faillure when == expected."""
        rule = num_greater(123.45)
        assert not rule(123.45)


class TestNumLess:
    """num_less test cases."""

    def test_ok_num_less(self):
        """Test Ok when input less than expected."""
        rule = num_less(123.45)
        assert rule(123)

    def test_ok_num_less_string(self):
        """Test Ok when input less than expected with string conversion."""
        rule = num_less(123.45)
        assert rule("123")

    def test_equal_not_num_less(self):
        """Test failure when input == expected."""
        rule = num_less(123.45)
        assert not rule(123.45)

    def test_not_num_less(self):
        """Test failure when input > expected."""
        rule = num_less(123.45)
        assert not rule(124)

    def test_not_num_less_string(self):
        """Test failure when input integer > expected."""
        rule = num_less(123.45)
        assert not rule("124")


class TestNumMax:
    """num_max test cases."""

    def test_ok_num_max(self):
        """Test Ok when input <= expected."""
        rule = num_max(xmax=1450.01)
        assert rule(1450.01)

    def test_ok_num_max_string(self):
        """Test Ok when input <= expected with string conversion."""
        rule = num_max(xmax=1450.01)
        assert rule("1450.01")

    def test_not_ok_num_max(self):
        """Test failure when input > expected."""
        rule = num_max(xmax=1450.01)
        assert not rule(1451)


class TestNumMin:
    """num_min test cases."""

    def test_ok_num_min_equal(self):
        """Test Ok when input >= expected."""
        rule = num_min(xmin=1450.01)
        assert rule(1450.01)

    def test_ok_num_min_equal_string(self):
        """Test Ok when input >= expected with string conversion."""
        rule = num_min(xmin=1450.01)
        assert rule("1450.01")

    def test_not_ok_num_min(self):
        """Test failure when input < minimum."""
        rule = num_min(xmin=1450.01)
        assert not rule(1450)


class TestNumNot:
    """num_not test cases."""

    def test_ok_num_not(self):
        """Test Ok when input != expected."""
        rule = num_not(in_value=1345)
        assert rule(5431)

    def test_ok_num_not_handle_string(self):
        """Test Ok when input != expected with string conversion."""
        rule = num_not(in_value=1345)
        assert rule("5431")

    def test_not_ok_num_not(self):
        """Test failure when input == expected."""
        rule = num_not(in_value=1345)
        assert not rule(1345)


class TestPrecision:
    """precision test cases."""

    def test_ok_precision(self):
        """Test Ok when input precision == expected."""
        rule = precision(in_value=8)
        assert rule(1234.5678)

    def test_ok_precision_handles_string(self):
        """Test Ok when input precision == expected with string conversion."""
        rule = precision(in_value=8)
        assert rule("1234.5678")

    def test_not_ok_precision(self):
        """Test failure when input precision !> expected."""
        rule = precision(in_value=8)
        assert not rule(1234.567)


class TestPrecisionGreater:
    """precision_greater test cases."""

    def test_ok_precision_greater(self):
        """Test Ok when input precision > in_value."""
        rule = precision_greater(in_value=8)
        assert rule(1234.56789)

    def test_ok_precision_greater_handles_string(self):
        """Test Ok when input precision > in_value with string conversion."""
        rule = precision_greater(in_value=8)
        assert rule("1234.56789")

    def test_not_ok_precision_greater(self):
        """Test failure when input precision <= in_value."""
        rule = precision_greater(in_value=8)
        assert not rule(1234.5678)


class TestPrecisionLess:
    """precision_less test cases."""

    def test_ok_precision_less(self):
        """Test Ok when input precision less that in_value."""
        rule = precision_less(in_value=8)
        assert rule(1234.567)

    def test_ok_precision_less_handles_string(self):
        """Test Ok when input precision < in_value with string conversion."""
        rule = precision_less(in_value=8)
        assert rule("1234.567")

    def test_not_ok_precision_less(self):
        """Test failure when input precision >= in_value."""
        rule = precision_less(in_value=8)
        assert not rule(1234.5678)


class TestPrecisionMax:
    """precision_max test cases."""

    def test_ok_precision_max(self):
        """Test Ok when precision <= in_value."""
        rule = precision_max(in_value=8)
        assert rule(1234.567)

    def test_ok_precision_max_handles_string(self):
        """Test Ok when precision <= in_value with string conversion."""
        rule = precision_max(in_value=8)
        assert rule("1234.567")

    def test_not_ok_precision_max(self):
        """Test failure when input precision > in_value."""
        rule = precision_max(in_value=8)
        assert not rule(1234.56789)


class TestPrecisionMin:
    """precision_min test cases."""

    def test_ok_precision_min(self):
        """Test Ok when input precision >= in_value."""
        rule = precision_min(in_value=8)
        assert rule(1234.5678)

    def test_ok_precision_min_handles_string(self):
        """Test Ok when input precision >= in_value with string conversion."""
        rule = precision_min(in_value=8)
        assert rule("1234.5678")

    def test_not_ok_precision_min(self):
        """Test failure when input precision < min precision."""
        rule = precision_min(in_value=8)
        assert not rule(1234.567)


class TestPrecisionNot:
    """precision_not test cases."""

    def test_ok_precision_not(self):
        """Test precision not matching as expected."""
        rule = precision_not(in_value=8)
        assert rule(1234.567)

    def test_ok_precision_not_handles_string(self):
        """Test precision not matching as expected with string conversion."""
        rule = precision_not(in_value=8)
        assert rule("1234.567")

    def test_not_ok_precision_not(self):
        """Test precision matching when not desired."""
        rule = precision_not(in_value=8)
        assert not rule(1234.5678)


class TestScale:
    """scale test cases."""

    def test_ok_scale(self):
        """Test scale of input matches expectation."""
        rule = scale(in_value=3)
        assert rule(1234.567)

    def test_ok_scale_handles_string(self):
        """Test handling of string input."""
        rule = scale(in_value=3)
        assert rule("1234.567")

    def test_not_ok_scale(self):
        """Test failure of input to match expected scale."""
        rule = scale(in_value=3)
        assert not rule(1234.5678)


class TestScaleGreater:
    """scale_greater test cases."""

    def test_ok_scale_greater(self):
        """Test scale of input > in_value."""
        rule = scale_greater(in_value=3)
        assert rule(1234.5678)

    def test_ok_scale_greater_handles_string(self):
        """Test handling of string input."""
        rule = scale_greater(in_value=3)
        assert rule("1234.5678")

    def test_not_ok_scale_greater(self):
        """Test failure of input scale > in_value."""
        rule = scale_greater(in_value=3)
        assert not rule(1234.567)


class TestScaleLess:
    """scale_less test cases."""

    def test_ok_scale_less(self):
        """Test scale of input > in_value."""
        rule = scale_less(in_value=3)
        assert rule(1234.56)

    def test_ok_scale_less_handles_string(self):
        """Test handling of string input."""
        rule = scale_less(in_value=3)
        assert rule("1234.56")

    def test_not_ok_scale_less(self):
        """Test failure of input scale > in_value."""
        rule = scale_less(in_value=3)
        assert not rule(1234.567)


class TestScaleMax:
    """scale_max test cases."""

    def test_ok_scale_max(self):
        """Test scale of input <= in_value."""
        rule = scale_max(in_value=3)
        assert rule(1234.56)

    def test_ok_scale_max_handles_string(self):
        """Test handling of string input."""
        rule = scale_max(in_value=3)
        assert rule("1234.56")

    def test_not_ok_scale_max(self):
        """Test failure of input scale <= in_value."""
        rule = scale_max(in_value=3)
        assert not rule(1234.5678)


class TestScaleMin:
    """scale_min test cases."""

    def test_ok_scale_min(self):
        """Test scale of input >= in_value."""
        rule = scale_min(in_value=3)
        assert rule(1234.567)

    def test_ok_scale_min_handles_string(self):
        """Test handling of string input."""
        rule = scale_min(in_value=3)
        assert rule("1234.567")

    def test_not_ok_scale_min(self):
        """Test failure of input scale >= in_value."""
        rule = scale_min(in_value=3)
        assert not rule(1234.56)


class TestScaleNot:
    """scale_not test cases."""

    def test_ok_scale_not(self):
        """Test scale of input != in_value."""
        rule = scale_not(in_value=3)
        assert rule(1234.56)

    def test_ok_scale_not_handles_string(self):
        """Test handling of string input."""
        rule = scale_not(in_value=3)
        assert rule("1234.5678")

    def test_not_ok_scale_not(self):
        """Test failure of input scale != in_value."""
        rule = scale_not(in_value=3)
        assert not rule(1234.567)
