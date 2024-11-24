# SkakiBot ♟️🤖

A command-line chess game where you play against an AI. Built with `python-chess` and OpenAI.

(In case you're wondering, "Skaki" is the Greek word for chess.)

## Setup

You need an OpenAI API key. Get it from [OpenAI API Keys](https://platform.openai.com/api-keys) and set it as an environment variable:

```bash
export OPENAI_API_KEY="your-openai-api-key"
```

## Running with Docker

1. ### Build the Docker Image

   Run the following command to build the Docker image:

   ```sh
   docker build -t skakibot .
   ```

2. ### Run the Docker Container

   Run the container and pass the OpenAI API key as an environment variable:

   ```sh
   docker run -e OPENAI_API_KEY="your_openai_api_key" -it skakibot
   ```

   The -it flag ensures the game runs interactively in your terminal.
