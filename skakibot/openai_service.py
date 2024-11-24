import openai


def get_openai_move(board, api_key, model):
    """
    Uses OpenAI to generate a move for the current board state.

    Args:
        board (chess.Board): The current chess board.
        api_key (str): The OpenAI API key.
        model (str): The OpenAI model to use (e.g., "gpt-4").

    Returns:
        str: The UCI move suggested by OpenAI.

    Raises:
        ValueError: If OpenAI fails to suggest a valid move.
    """
    try:
        openai.api_key = api_key

        board_fen = board.fen()
        legal_moves = ", ".join(move.uci() for move in board.legal_moves)

        response = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": (
                    "You are an expert chess player and assistant. Your task is to "
                    "analyse chess positions and suggest the best move in UCI format."
                )},
                {"role": "user", "content": (
                    "The current chess board is given in FEN notation:\n"
                    f"{board_fen}\n\n"
                    "The following are the legal moves for this position:\n"
                    f"{legal_moves}\n\n"
                    "Analyse the position and suggest the best possible move from the list of legal moves. "
                    "Respond with a single UCI move, such as 'e2e4'. Do not provide any explanations."
                )}
            ])

        suggested_move = response.choices[0].message.content.strip()
        return suggested_move

    except Exception as e:
        raise ValueError(f"OpenAI API error: {e}")
