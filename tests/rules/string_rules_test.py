"""string rules tests."""

from csv_blueprint.rules.string import (
    exact_value,
    is_lowercase,
    is_sentence,
    is_trimmed,
    is_uppercase,
    is_uuid,
    length,
    length_greater,
    length_less,
    length_max,
    length_min,
    length_not,
    not_empty,
    regex,
)


class TestIsTrimmed:
    """Test is_trimmed rule."""

    def test_ok_trimmed_string(self):
        """Test is_trimmed ok."""
        rule = is_trimmed(b=True)
        assert rule("no space")

    def test_inverted_trimmed_string(self):
        """Test is_trimmed not ok because b=False."""
        rule = is_trimmed(b=False)
        assert not rule("no space")

    def test_not_ok_untrimmed_string(self):
        """Test is_trimmed not ok."""
        rc = is_trimmed(b=True)
        assert not rc(" some space")


class TestIsUUID:
    """Test is_uuid."""

    def test_true_valid_uuid(self):
        """Test expected result for valid uuid."""
        rule = is_uuid(b=True)
        assert rule("b7056d67-2acc-4f1e-902e-f1eb1e4c7cfd")

    def test_inverted_valid_uuid(self):
        """Test expected result for valid uuid."""
        rule = is_uuid(b=False)
        assert not rule("b7056d67-2acc-4f1e-902e-f1eb1e4c7cfd")

    def test_false_invalid_uuid(self):
        """Test expected result for invalid uuid."""
        rule = is_uuid(b=True)
        assert not rule("invalid uuid")


class TestIsUppercase:
    """is_uppercase test cases."""

    def test_expected_valid_uppercase(self):
        """Test expected result for uppercase letter."""
        rule = is_uppercase(b=True)
        assert rule("UPPER CASE .")

    def test_inverted_valid_uppercase(self):
        """Test expected result for uppercase letter."""
        rule = is_uppercase(b=False)
        assert not rule("UPPER CASE .")

    def test_expected_invalid_uppercase(self):
        """Test expected result for invalid uppercase letter."""
        rule = is_uppercase(b=True)
        assert not rule("Invalid UPPERCase. ")


class TestNotEmpty:
    """not_empty test cases."""

    def test_ok_not_empty(self):
        """Test expected result valid not_empty."""
        rule = not_empty(b=True)
        assert rule("Some values")
        assert rule(0)
        assert rule("0")
        assert rule(" ")

    def test_inverted_not_empty(self):
        """Test expected result valid not_empty."""
        rule = not_empty(b=False)
        assert not rule("Some values")
        assert rule("")

    def test_not_ok_not_empty(self):
        """Test expected false result invalid not_empty."""
        rule = not_empty(b=True)
        assert not rule("")
        assert not rule(None)


class TestRegex:
    """regex test cases."""

    def test_ok_matches_regex(self):
        """Test email regex."""
        rule = regex(r"^[a-zA-Z0-9. _-]+@[a-zA-Z0-9. -]+\.[a-zA-Z]{2,4}$")
        assert rule("developer@wheredevelopersmeet.com")

    def test_not_ok_invalid_email_for_email_regex(self):
        """Test email regex with invalid email."""
        rule = regex(r"^[a-zA-Z0-9. _-]+@[a-zA-Z0-9. -]+\.[a-zA-Z]{2,4}$")
        assert not rule("developerwheredevelopersmeet.com")


class TestLowercase:
    """is_lowercase test cases."""

    def test_ok_lowercase(self):
        """Test expected ok for lowercase."""
        rule = is_lowercase(b=True)
        assert rule("lowercase only.")

    def test_inverted_lowercase(self):
        """Test expected ok for lowercase."""
        rule = is_lowercase(b=False)
        assert not rule("lowercase only.")

    def test_not_lowercase(self):
        """Test expected failure for lowercase."""
        rule = is_lowercase(b=True)
        assert not rule("NOT lowercae")


class TestExactValue:
    """exact_value test cases."""

    def test_ok_exact_value(self):
        """Test expected ok for exact_value."""
        rule = exact_value("Suya or Berbeque.")
        assert rule("Suya or Berbeque.")

    def test_not_ok_exact_value(self):
        """Test expected failure for exact value."""
        rule = exact_value("Suya or Berbeque.")
        assert not rule("Berbeque.")


class TestIsSentence:
    """is_sentence (phrase :)) test cases."""

    def test_ok_is_sentence(self):
        """Test ok multiple words input."""
        rule = is_sentence(b=True)
        assert rule("oro Yoruba.")

    def test_inverted_is_sentence(self):
        """Test ok multiple words input."""
        rule = is_sentence(b=False)
        assert not rule("oro Yoruba.")

    def test_not_ok_sentence(self):
        """Test not ok single word input."""
        rule = is_sentence(b=True)
        assert not rule("oropo.")


class TestLength:
    """length test cases."""

    def test_ok_length(self):
        """Test ok length."""
        rule = length(9)
        assert rule("123456789")

    def test_not_ok_length(self):
        """Test not ok input length not matching."""
        rule = length(9)
        assert not rule("12345678")


class TestLengthGreater:
    """length_greater test cases."""

    def test_ok_length_greater(self):
        """Test ok length_greater."""
        rule = length_greater(in_value=5)
        assert rule("123456")

    def test_not_ok_length_greater(self):
        """Test not ok input length equal in_value."""
        rule = length_greater(in_value=5)
        assert not rule("12345")


class TestLengthMax:
    """length_max test cases."""

    def test_ok_length_max(self):
        """Test ok length_max."""
        rule = length_max(in_value=5)
        assert rule("12345")

    def test_not_ok_length_max(self):
        """Test not ok input > length_max."""
        rule = length_max(in_value=5)
        assert not rule("123456")


class TestLengthLess:
    """length_less test cases."""

    def test_ok_length_less(self):
        """Test ok length_max."""
        rule = length_less(in_value=5)
        assert rule("1234")

    def test_not_ok_length_less(self):
        """Test not ok input > length_max."""
        rule = length_less(in_value=5)
        assert not rule("12345")


class TestLengthMin:
    """length_min test cases."""

    def test_ok_length_min(self):
        """Test ok when length >= in_value."""
        rule = length_min(in_value=5)
        assert rule("12345")

    def test_not_ok_length_min(self):
        """Test not ok when not length >= in_value."""
        rule = length_min(in_value=5)
        assert not rule("1234")


class TestLengthNot:
    """length_not test cases."""

    def test_ok_length_not(self):
        """Test ok when length_not in_value."""
        rule = length_not(in_value=10)
        assert rule("not exactly ten")

    def test_not_ok_length_not(self):
        """Test fails when exactly in_value."""
        rule = length_not(in_value=10)
        assert not rule("exactly 10")
