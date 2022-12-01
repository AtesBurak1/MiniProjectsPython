import time,random


class Player:
    def __init__(self,letter):
        #letter is o or x
        self.letter = letter

    # we want all players to get their next move given agame
    def get_move(self,game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        square = random.choice(game.available_moves())
        return square
        


class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these are successful, tthen yay
            except ValueError:
                    print("Invalid square. Try again.")

        return val

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # list for 3x3 board
        self.current_winner = None #winner

    def print_board(self):
        #this is just get rows(triples)
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0| 1 |2 etc
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        list = [i for i, spot in enumerate(self.board) if spot == ' ']
        return list
        #yapılabilir hameleler
    
    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        print(square)
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # 3 in a row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check cloumn
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # check diagnols
        #but only if the square is an even number
        if square%2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4 ,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4 ,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

def play(game, x_player, o_player, print_game= True):
    if print_game:
        game.print_board_nums()

    letter = 'X'
    #starting letter


    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        #define a function to play
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') # just emppy line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')     
                return letter           


            letter = 'O' if letter == 'X' else 'X' # switches players
        
        time.sleep(0.8)


    if print_game:
            print('It\'s a tie!')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)