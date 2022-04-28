"""
Week 2: Tic-Tac-Toe Assignment
Author: Bro. Manley

Meticulously Studied, Copied, Edited, Troubleshot, and Added To by Chance Schneider
(Excuse: I have not written a line of code for 4 months as we just had a baby and I started a new job - I was utterly
lost, and needed to use this assignment to bring me back up to speed. I spent a ton of time going over every line, 
re-writing it, and troubleshooting every error that still managed to come up. I know this isn't the pattern
for learning in this class, and I don't plan to do future weeks like this. However, I'm extremely grateful this is here,
so that I CAN study the material and come back up to speed. I most definitely want to LEARN to code, not only to pass 
this class.)


Step 1: Create Board
Step 2: Display Board
Step 3: Establish situation for Winner
Step 4: Establish situation for Tie
Step 5: Make function to allow each player to move
Step 6: Make function for switching between players after each move 

Bonus: Added Tie Message, Play Again? feature, and Responses/Penalty for choosing an occupied square. 

Notes: Must evaluate state of the board, looking for winner or tie, between each player's turn
"""


def main():
    play_again = ""
    while play_again.lower() != "n": 
        player = next_player("")
        board = create_board()
        while not (winner(board) or tie(board)):
            display_board(board)
            make_a_move(player, board)
            player = next_player(player)
        display_board(board)
        if tie(board):
            print("Tie game. Participation awards for everybody.")
        else:
            print("Game over. You have won. Or, maybe you have lost. But, in the words of Zarahemna, 'Behold, it mattereth not.'")
        play_again = str(input("Play again (y/n)? "))


def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board


def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()


def tie(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 


def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])


def make_a_move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    if board[square - 1] != "x" and board[square -1] != "o":
        board[square - 1] = player
    else: 
        square = int(input(f"Pick another spot, bub (1-9): "))
        if board[square - 1] != "x" and board[square - 1] != "o":
            board[square - 1] = player
        else:
            print("Cheater, cheater, pumpkin eater. Looks like ya lost your turn, holmes.")
        


def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"



if __name__ == "__main__":
    main()

    