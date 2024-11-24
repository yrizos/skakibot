import pytest
from unittest.mock import patch
from skakibot.config import get_openai_key, get_openai_model


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


def test_get_openai_model_default():
    """
    Test that get_openai_model returns the default model if it's not set in the environment.
    """
    with patch("os.getenv", side_effect=lambda key, default=None: default):
        model = get_openai_model()
        assert model == "gpt-3.5-turbo"


def test_get_openai_model_custom():
    """
    Test that get_openai_model returns the model if it's set in the environment.
    """
    with patch("os.getenv", return_value="gpt-4.0"):
        model = get_openai_model()
        assert model == "gpt-4.0"
