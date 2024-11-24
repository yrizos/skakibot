import chess
from skakibot.config import get_openai_key, get_openai_model
from skakibot.cli import CLI
from skakibot.openai_service import get_openai_move


def handle_endgame(board, cli):
    """
    Handles the endgame logic by determining the game state and displaying an appropriate message.
    """
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


def handle_user_move(board, cli):
    """
    Handles user input, validates the move, and updates the board.
    Returns a tuple (success, message), where success is a boolean indicating
    whether the move was valid, and message is the status message to display.
    """
    user_input = cli.get_user_input()
    if user_input.lower() == 'exit':
        return False, "exit"

    try:
        move = chess.Move.from_uci(user_input)
        if move in board.legal_moves:
            board.push(move)
            return True, f"Move '{user_input}' played."
        else:
            return False, "Invalid move. Please enter a valid move."
    except ValueError:
        return False, "Invalid move format. Use UCI format like 'e2e4'."


def main():
    """
    Main function for the CLI chess game.
    Handles user input, validates moves, and updates the board.
    """
    openai_key = get_openai_key()
    openai_model = get_openai_model()
    cli = CLI(
        welcome_message=f"Welcome to Skakibot! Using OpenAI model: {openai_model}")
    board = chess.Board()
    current_message = ""

    while not board.is_game_over():
        cli.display_board(board, current_message)

        success, message = handle_user_move(board, cli)
        if message == "exit":
            break

        current_message = message
        if not success:
            continue

        if not board.is_game_over():
            try:
                ai_move_uci = get_openai_move(board, openai_key, openai_model)
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

    handle_endgame(board, cli)
