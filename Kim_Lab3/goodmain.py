"""
Refactored version of badmain.py about tic-tac-toe game

:author: Chris Hegang Kim
:note: I affirm that I have carried out the attached academic endeavors with full academic honesty,
in accordance with the Union College Honor Code and the course syllabus.

:reflection: 1. Because it was on a global scope, some variables such as board and winner were used throughout the code
                without any orders and rules.
             2. I grouped the main-line into a single function called main(), and modified related codes when changing
                global variables to local variables such as removing globals and adding parameters and return statements.
"""
def print_board(board):
    """
    Prints a string for the board which is originally a list

    :param: the list for the board
    :return:
    """
    num_rows = len(board)
    num_cols = len(board[0])
    for row_num, row in enumerate(board):
        row_str = ''
        for col_num, marker in enumerate(row):
            row_str += marker
            if col_num < num_cols - 1:
                row_str += ' | '
        print(row_str)
        if row_num < num_rows - 1:
            print('---------')


def row_all_same(the_board, row):
    """
    Checks whether the row of the board is in all same character

    :param the_board: a list for the board
    :param row: an integer for the index for each row
    :return: True if the row is in all same character
    """
    return (the_board[row][0] == the_board[row][1] == the_board[row][2])


def column_all_same(column):
    """
    Checks whether the column is in all same character

    :param column: a string for each column
    :return: True if the column is in all same character
    """
    return (column[0] == column[1] == column[2])


def diagonal_all_same(diagonal):
    """
    Checks whether the diagonal is in all same character

    :param diagonal: a list with elements of the diagonal
    :return: True if the diagonal is in all same character
    """
    return (diagonal[0] == diagonal[1] == diagonal[2])


def get_back_slash(board):
    """
    Returns a list with elements of the back-slash diagonal

    :param: a list for the board
    :return: a list with elements of the diagonal
    """
    return [board[i][i] for i in range(len(board))]


def get_forward_slash(board):
    """
    Returns a list with elements of the forward-slash diagonal

    :param: a list for the board
    :return: a list with elements of the diagonal
    """
    return [board[len(board)-i-1][i] for i in range(len(board))]


def columns(board):
    """
    Returns a list with elements for columns on the board

    :param board: a list for the board
    :return: a list with elements for columns on the board
    """
    num_cols = len(board[0])
    num_rows = len(board)
    
    to_return = []
    
    for i in range(num_cols):
        col_str = ''
        for j in range(num_rows):
            col_str += board[j][i]
        to_return.append(col_str)
    return to_return


def check_winner(board):
    """
    Checks possible winning scenarios and determines the winner

    :param: a list for the board
    :return: a string for the winner based on possible scenarios
    """
    for row_num, row in enumerate(board):
        if row_all_same(board, row_num):
            winner = board[row_num][0]
            return winner
        
    for col in columns(board):
        if column_all_same(col):
            winner = col[0]
            return winner
    
    if diagonal_all_same(get_back_slash()):
        winner = board[0][0]
        return winner
    
    if diagonal_all_same(get_forward_slash()):
        winner = board[2][0]
        return winner


def get_board_from_file(filename):
    """
    Get a board from the file and creates a list for the board

    :param filename: a file for the board
    :return: a list for the board
    """
    board_list = []
    board_file = open(filename,"r")
    for line in board_file:
        board_list.append(line.strip())
    board_file.close()
    return board_list

def main():
    """
    Starts the entire program and prints the winner

    :return:
    """
    inputfile = 'input.txt'
    board = get_board_from_file(inputfile)

    print_board(board)

    winner = check_winner(board)

    if winner != '':
        print(winner + ' WINS!!!!')
    else:
        print("TIE GAME!!!!")

if __name__ == "__main__":
    main()
