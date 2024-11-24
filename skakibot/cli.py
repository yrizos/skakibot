import os


class CLI:
    def __init__(self, welcome_message="Welcome to Skakibot!"):
        """
        Initializes the CLI with a welcome message.
        """
        self.welcome_message = welcome_message

    @staticmethod
    def clear_display():
        """Clears the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_board(self, board, message=""):
        """
        Displays the chess board along with a welcome message and an optional status message.
        """
        self.clear_display()
        print(f"{self.welcome_message}\nType 'exit' to quit the game.\n")
        print(board)
        if message:
            print(f"\n{message}\n")
        else:
            print("\n")

    @staticmethod
    def get_user_input():
        """
        Prompts the user for input.
        Returns:
            str: The user's input.
        """
        return input("Enter your next move (e.g., e2e4): ").strip()

    @staticmethod
    def show_error(message):
        """
        Displays an error message.
        """
        print(f"Error: {message}")

    @staticmethod
    def show_game_over_message(result_message):
        """
        Displays the game-over message.
        """
        print(f"\n{result_message}\n")
        print("Thanks for playing SkakiBot. Goodbye!")
