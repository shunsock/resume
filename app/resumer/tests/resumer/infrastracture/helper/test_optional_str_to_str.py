import pytest

from resumer.infrastracture.helper.optional_str_to_str import optional_str_to_str


@pytest.mark.parametrize(
    "value, expected",
    [
        (None, ""),
        ("", ""),
        ("test", "test"),
    ],
)
def test_optional_str_to_str(value, expected):
    assert optional_str_to_str(value) == expected
