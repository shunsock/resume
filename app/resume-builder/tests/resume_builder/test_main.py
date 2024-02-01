import pytest

from resume_builder.main import Hello


@pytest.mark.parametrize(
    "message",
    [
        pytest.param("Hello World!", id="Hello World!"),
        pytest.param("Hello World!!", id="Hello World!!"),
    ],

)
def test_hello(message: str):
    hello = Hello(message=message)
    assert hello.hello() == message
