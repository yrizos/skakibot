import os


def get_openai_key() -> str:
    """
    Retrieves the OpenAI API key from the environment.
    Raises an error if the key is not set.
    """
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise EnvironmentError(
            "OpenAI API key is not set. Please set 'OPENAI_API_KEY' in the environment.")
    return key


def get_openai_model():
    return os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
