"""Boolean rules test cases."""

from csv_blueprint.rules.bool import is_bool


class TestIsBool:
    """is_bool test cases."""

    def test_ok_bool_rule(self):
        """Test handling of boolean."""
        rule = is_bool(b=True)
        assert rule(value=True)

    def test_ok_bool_rule_false(self):
        """Test handling of False boolean."""
        rule = is_bool(b=True)
        assert rule(value=False)

    def test_ok_inverted_bool_rule(self):
        """Test handling of boolean."""
        rule = is_bool(b=False)
        assert not rule(value=True)

    def test_handle_boolean_string(self):
        """Test handling of string boolean."""
        rule = is_bool(b=True)
        assert rule("True")
