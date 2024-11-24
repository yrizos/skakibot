def main():
    """
    Main function for the CLI game. Handles user input for the next move.
    """
    print("Welcome to SkakiBot! Type 'exit' to quit the game.")

    while True:
        user_input = input("Enter your next move: ").strip()

        if user_input.lower() == 'exit':
            print("Thanks for playing SkakiBot. Goodbye!")
            break

        if not user_input:
            print("Move cannot be empty. Please try again.")
            continue

        print(f"You entered: {user_input}")
