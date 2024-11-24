import os
import chess


def clear_display():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


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
        except ValueError:
            current_message = "Invalid move format. Use UCI format like 'e2e4'."

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
