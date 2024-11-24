import os
import chess
import openai
from skakibot.config import get_openai_key, get_openai_model
from skakibot.cli import CLI


def get_openai_move(board):
    """
    Uses OpenAI to generate a move for the current board state.
    """
    openai.api_key = get_openai_key()
    board_fen = board.fen()
    legal_moves = ", ".join(move.uci() for move in board.legal_moves)

    response = openai.chat.completions.create(
        model=get_openai_model(),
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


def main():
    """
    Main function for the CLI chess game.
    Handles user input, validates moves, and updates the board.
    """
    model = get_openai_model()
    cli = CLI(
        welcome_message=f"Welcome to Skakibot! Using OpenAI model: {model}")
    board = chess.Board()
    current_message = ""

    while not board.is_game_over():
        cli.display_board(board, current_message)

        user_input = cli.get_user_input()
        if user_input.lower() == 'exit':
            break

        try:
            move = chess.Move.from_uci(user_input)
            if move in board.legal_moves:
                board.push(move)
                current_message = f"Move '{user_input}' played."
            else:
                current_message = "Invalid move. Please enter a valid move."
                continue
        except ValueError:
            current_message = "Invalid move format. Use UCI format like 'e2e4'."
            continue

        if not board.is_game_over():
            try:
                ai_move_uci = get_openai_move(board)
                ai_move = chess.Move.from_uci(ai_move_uci)
            except Exception as e:
                cli.show_error(f"Error with OpenAI: {str(e)}")
                break

            if ai_move in board.legal_moves:
                board.push(ai_move)
                current_message = f"OpenAI played '{ai_move_uci}'."
            else:
                cli.show_error(
                    f"OpenAI suggested an invalid move: '{ai_move_uci}'.")
                break

    if board.is_checkmate():
        cli.show_game_over_message("Checkmate! The game is over.")
    elif board.is_stalemate():
        cli.show_game_over_message("Stalemate! The game is a draw.")
    elif board.is_insufficient_material():
        cli.show_game_over_message("Draw due to insufficient material.")
    elif board.is_seventyfive_moves():
        cli.show_game_over_message("Draw due to the seventy-five-move rule.")
    else:
        cli.show_game_over_message("Game ended.")
