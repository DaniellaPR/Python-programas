import random

def initialize_cards():
    # Create a list of card pairs
    cards = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] * 2
    random.shuffle(cards)
    return cards

def display_board(board):
    for row in board:
        print(" ".join(row))

def play_game():
    cards = initialize_cards()
    board_size = 4  # Change this to adjust the size of the board
    board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
    matched_pairs = 0

    while matched_pairs < len(cards) // 2:
        display_board(board)

        # Get user input for the first card
        print("\nEnter the coordinates of the first card (row and column, separated by space):")
        row1, col1 = map(int, input().split())
        while board[row1][col1] != ' ':
            print("Card already revealed. Try again.")
            row1, col1 = map(int, input().split())

        board[row1][col1] = cards[row1 * board_size + col1]

        display_board(board)

        # Get user input for the second card
        print("\nEnter the coordinates of the second card (row and column, separated by space):")
        row2, col2 = map(int, input().split())
        while board[row2][col2] != ' ':
            print("Card already revealed. Try again.")
            row2, col2 = map(int, input().split())

        board[row2][col2] = cards[row2 * board_size + col2]

        display_board(board)

        # Check the cards match
        if cards[row1 * board_size + col1] == cards[row2 * board_size + col2]:
            print("Match found!")
            matched_pairs += 1
        else:
            print("No match. Try again.")
            board[row1][col1] = ' '
            board[row2][col2] = ' '

    print("\nCongratulations! You've matched all pairs.")

if __name__ == "__main__":
    play_game()