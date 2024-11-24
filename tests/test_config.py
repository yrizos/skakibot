
import pytest
from unittest.mock import patch
from skakibot.config import get_openai_key


def test_get_openai_key_success():
    """
    Test that get_openai_key returns the key if it's set in the environment.
    """
    with patch("os.getenv", return_value="fake-openai-key"):
        key = get_openai_key()
        assert key == "fake-openai-key"


def test_get_openai_key_missing():
    """
    Test that get_openai_key raises an error if the key is not set.
    """
    with patch("os.getenv", return_value=None):
        with pytest.raises(EnvironmentError) as exc_info:
            get_openai_key()
        assert str(
            exc_info.value) == "OpenAI API key is not set. Please set 'OPENAI_API_KEY' in the environment."


def test_get_openai_key_empty():
    """
    Test that get_openai_key raises an error if the key is an empty string.
    """
    with patch("os.getenv", return_value=""):
        with pytest.raises(EnvironmentError) as exc_info:
            get_openai_key()
        assert str(
            exc_info.value) == "OpenAI API key is not set. Please set 'OPENAI_API_KEY' in the environment."
