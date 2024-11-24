import unittest
from unittest.mock import patch, call
from io import StringIO
import chess
import os
from skakibot.cli import CLI


class TestCLI(unittest.TestCase):

    @patch('os.system')
    def test_clear_display(self, mock_system):
        CLI.clear_display()
        mock_system.assert_called_once_with(
            'cls' if os.name == 'nt' else 'clear')

    @patch('builtins.print')
    @patch('os.system')
    def test_display_board(self, mock_system, mock_print):
        cli = CLI()
        board = chess.Board()
        cli.display_board(board, "Test message")

        mock_system.assert_called_once_with(
            'cls' if os.name == 'nt' else 'clear')
        mock_print.assert_has_calls([
            call(f"{cli.welcome_message}\nType 'exit' to quit the game.\n"),
            call(board),
            call("\nTest message\n")
        ])

    @patch('builtins.input', return_value='e2e4')
    def test_get_user_input(self, mock_input):
        user_input = CLI.get_user_input()
        self.assertEqual(user_input, 'e2e4')


if __name__ == '__main__':
    unittest.main()
