# SkakiBot ♟️🤖

A command-line chess game where you play against an AI, built with `python-chess` and OpenAI. I've documented my process in: ["Building a Chess Game with Python and OpenAI"](https://dev.to/yrizos/building-a-chess-game-with-python-and-openai-3knn).

(And yes, "Skaki" is the Greek word for chess)

## Setup

You need an OpenAI API key. Get it from [OpenAI API Keys](https://platform.openai.com/api-keys) and set it as an environment variable:

```bash
export OPENAI_API_KEY="your-openai-api-key"
```

The default model is `gpt-3.5-turbo`. You can override this by setting `OPENAI_MODEL`:

```bash
export OPENAI_MODEL="gpt-4.0-mini"
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
