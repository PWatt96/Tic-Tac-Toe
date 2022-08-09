from sys import stderr


class Move:
    """"Class to encapsulate the data needed for a move"""

    def __init__(self, x: int, y: int, token: str):
        self.x = x
        self.y = y
        self.value = token

    pass


class Board:

    def __init__(self):
        self.state = [[' ' for i in range(3)] for j in range(3)]

    def print_board(self):
        for i in range(3):
            for j in range(3):
                print(self.state[i][j], end=' ')
                if j < 2:
                    print('|', end=' ')
                else:
                    if i != 2:
                        print('\n_   _   _')
                if i == 2 and j == 2:
                    print("")

    def make_move(self, move: Move) -> bool:
        """Places either an X or O at the coordinates (x, y). The value
        parameter determines whether an X or O is placed.
        If there is already a value a (x, y), then this returns false, otherwise it returns true."""
        if self.state[move.x][move.y] != ' ':
            return False
        self.state[move.x][move.y] = move.value
        return True

    def evaluate_board_win(self) -> bool:
        """Checks whether the game is over (i.e. there are three X's or three O's in a row)"""
        # need to check all horizontal lines
        for i in range(3):
            if self.state[i][0] == self.state[i][1] == self.state[i][2] != ' ':
                return True

        # need to check all vertical lines
        for j in range(3):
            if self.state[0][j] == self.state[1][j] == self.state[2][j] != ' ':
                return True

        # need to check both diagonal lines
        if self.state[0][0] == self.state[1][1] == self.state[2][2] != ' ':
            return True

        if self.state[0][2] == self.state[1][1] == self.state[2][0] != ' ':
            return True

        return False


class Player:
    """A player has a token which determines whether they will place down an X or an O. Player 1 has X and
    player 2 has O."""

    def __init__(self, player_number: int):
        if player_number == 1:
            self.token = 'X'
        else:
            self.token = 'O'

    def get_move(self) -> Move:
        """Asks the user for the (x, y) coordinates where they want to place their token."""
        x = self.__get_input("x")
        y = self.__get_input("y")
        move = Move(x, y, self.token)
        return move

    @staticmethod
    def __get_input(coordinate: str) -> int:
        while True:
            try:
                x = int(input("Please enter the {0}-coordinate you want to place your token at: ".format(coordinate)))
                # want to leave the loop if x is an integer and between 0 and 2
                if 0 <= x <= 2:
                    break
            except ValueError:
                print("Please enter a number between 0 and 2 for the {0}-coordinate".format(coordinate))
        return x

    @staticmethod
    def __check_coordinate_input_valid(coordinate):
        while not isinstance(coordinate, int):
            print("Please enter a number")
            coordinate = input("Please enter the x-coordinate you want to place your token at.")


class Game:
    """Allows two human users to play a game of tic-tac-toe."""

    @staticmethod
    def play_tic_tac_toe():
        p1 = Player(1)
        p2 = Player(2)
        board = Board()
        current_player = 1
        print("Welcome to tic tac toe....")
        while True:
            if current_player == 1:
                player = p1
                current_player = 2
            else:
                player = p2
                current_player = 1
            board.print_board()
            move = player.get_move()
            while not board.make_move(move):
                print('That space is already taken, please enter the coordinates for another space.')
                move = player.get_move()
            if board.evaluate_board_win():
                board.print_board()
                break
        print("Game Over!...Player {0} won!".format(player.token))
