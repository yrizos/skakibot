import os
import chess
import openai
from skakibot.config import get_openai_key


def clear_display():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_openai_move(board):
    """
    Uses OpenAI to generate a move for the current board state.
    """
    openai.api_key = get_openai_key()
    board_fen = board.fen()

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": (
                "You are an expert chess player and assistant. Your task is to "
                "analyse chess positions and suggest the best move in UCI format."
            )},
            {"role": "user", "content": (
                "The current chess board is given in FEN notation:\n"
                f"{board_fen}\n\n"
                "Analyse the position and suggest the best possible move. Respond "
                "with a single UCI move, such as 'e2e4'. Do not provide any explanations."
            )}
        ])

    suggested_move = response.choices[0].message.content.strip()
    return suggested_move


def main():
    """
    Main function for the CLI chess game.
    Handles user input, validates moves, and updates the board.
    """
    welcome_message = "Welcome to SkakiBot! Type 'exit' to quit the game."
    board = chess.Board()
    current_message = ""

    while not board.is_game_over():
        clear_display()
        print(welcome_message)
        print(board)
        if current_message:
            print(f"\n{current_message}")
        else:
            print("\n")

        user_input = input("Enter your next move (e.g., e2e4): ").strip()

        if user_input.lower() == 'exit':
            print("Thanks for playing SkakiBot. Goodbye!")
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

        try:
            ai_move_uci = get_openai_move(board)
            ai_move = chess.Move.from_uci(ai_move_uci)
            if ai_move in board.legal_moves:
                board.push(ai_move)
                current_message = f"OpenAI played '{ai_move_uci}'."
            else:
                current_message = "OpenAI suggested an invalid move. Skipping its turn."
        except Exception as e:
            print(f"Error with OpenAI: {str(e)}")
            print("The game is ending due to an error with OpenAI. Goodbye!")
            break

    if board.is_checkmate():
        print("Checkmate! The game is over.")
    elif board.is_stalemate():
        print("Stalemate! The game is a draw.")
    elif board.is_insufficient_material():
        print("Draw due to insufficient material.")
    elif board.is_seventyfive_moves():
        print("Draw due to the seventy-five-move rule.")
    else:
        print("Game ended.")
