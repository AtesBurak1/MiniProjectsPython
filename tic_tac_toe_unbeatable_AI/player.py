import math
import random


class Player:
    def __init__(self, letter):
        #letter is o or x
        self.letter = letter

    # we want all players to get their next move given agame
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True  # if these are successful, tthen yay
            except ValueError:
                print("Invalid square. Try again.")

        return val


class SuperComputer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # if all the borad is empty then pick a random num
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            # board based minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, game, player):
        our_player = self.letter
        other_player = 'O' if player == 'X' else 'X'  # give letter for the other player

        # base case for recursion
        if game.current_winner == other_player:
            return {
                'position': None,
                'score': 1 * (game.num_empty_squares() + 1) if other_player == our_player else -1 * (game.num_empty_squares() + 1)
            }
        elif not game.empty_squares():  # not empty squares
            return {'position': None, 'score': 0}

        if player == our_player:
            # initilaze score to minimum
            best = {'position': None, 'score': -math.inf}
        else:
            # initilaze score to maximum
            best = {'position': None, 'score': math.inf}

        for possible_move in game.available_moves():

            game.make_move(possible_move, player)

            sim_score = self.minimax(game, other_player)

            game.board[possible_move] = ' '
            game.current_winner = None
            sim_score['position'] = possible_move

            if player == our_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
