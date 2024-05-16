"""Enum rules test cases."""

from csv_blueprint.rules.enum import allow_values, not_allow_values


class TestAllowValues:
    """allow_values test cases."""

    def test_ok_allow_values(self):
        """Test ok when value in whitelist."""
        rule = allow_values(whilelist=["a", "b", "c"])
        assert rule("b")

    def test_ok_allow_values_integers(self):
        """Test ok when value in whitelist."""
        rule = allow_values(whilelist=[5, 10, 15])
        assert rule(15)

    def test_not_ok_allow_values(self):
        """Test failure when value not in whitelist."""
        rule = allow_values(whilelist=["a", "b", "c"])
        assert not rule("d")


class TestNotAllowValues:
    """not_allow_values test cases."""

    def test_ok_not_allow_values(self):
        """Test ok when value not in blacklist."""
        rule = not_allow_values(blacklist=["a", "b", "c"])
        assert rule("d")

    def test_ok_not_allow_values_integers(self):
        """Test ok when value not in blacklist."""
        rule = not_allow_values(blacklist=[5, 10, 15])
        assert rule(20)

    def test_not_ok_not_allow_values(self):
        """Test failure when value in blacklist."""
        rule = not_allow_values(blacklist=["a", "b", "c"])
        assert not rule("c")
