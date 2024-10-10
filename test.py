import unittest
from unittest.mock import patch
from calc_game import operations, gameplay, equations

class TestCalculatorGame(unittest.TestCase):
    
    # Test the operations function
    def test_operations(self):
        self.assertEqual(operations("/", 10, 2), 5)
        self.assertEqual(operations("*", 3, 4), 12)
        self.assertEqual(operations("+", 5, 5), 10)
        self.assertEqual(operations("-", 9, 4), 5)
        self.assertIsNone(operations("invalid_operator", 1, 1))

    # Test the equations function with mocked inputs and random values
    @patch('random.uniform', side_effect=[5, 2, 8, 4, 7, 3, 9, 3, 1, 8])  # Mock random numbers
    @patch('random.choice', side_effect=["+", "-", "*", "/", "+"])  # Mock operator selection
    @patch('builtins.input', side_effect=["7", "4", "21", "3", "2"])  # Mock user inputs
    def test_equations(self, mock_input, mock_randrange, mock_choice):
        score = equations()  # Call the equations function
        self.assertEqual(score, 4)  # Check if the score matches the expected value

    # Test gameplay function with mocked inputs
    @patch('random.uniform', side_effect=[5, 2, 8, 4, 7, 3, 9, 3, 1, 8])  # Mock random numbers
    @patch('random.choice', side_effect=["+", "-", "*", "/", "+"])  # Mock operator selection
    @patch('builtins.input', side_effect=["7", "4", "21", "3", "2"])  # Mock user inputs
    def test_gameplay(self, mock_input, mock_randrange, mock_choice):
        result = gameplay()  # Call the gameplay function
        self.assertEqual(result, "Nice one!!")  # Check the returned message

    # Test if wrong input is handled correctly
    @patch('random.uniform', side_effect=[5, 2, 8, 4, 7, 3, 9, 3, 1, 8])  # Mock random numbers
    @patch('random.choice', side_effect=["+", "-", "*", "/", "+"])  # Mock operator selection
    @patch('builtins.input', side_effect=["wrong_input", "2.5", 45, "hh", 9])  # Mock user inputs
    def test_gameplay_with_wrong_input(self, mock_uniform, mock_choice, mock_input):
        result = gameplay()  # Call the gameplay function
        self.assertEqual(result, "Try again!!")  # Check the returned message

# Running the tests
if __name__ == '__main__':
    unittest.main()
