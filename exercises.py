class Game():

    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
    
    def play_game(self):
        print('Welcome to TickyTackyToesy! Let\'s play!')

    def print_board(self):
        b = self.board
        print(f"""
            A   B   C
        1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
        ----------
        2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
        ----------
        3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)
    
    def print_message(self):
        if self.tie is True: 
            print('Tie game!')
        elif self.winner is not None: 
            print(f'{self.winner} wins the game!')
        else: 
            print(f'It\'s player {self.turn}\'s turn.')

    def get_move(self):
         while True: 
            move = input(f'Enter a valid move (example: A1): '.lower())

            if move not in self.board.keys():
                print('Invalid move. Please enter a valid move (e.g., A1, B2, C3).')
                continue
            if self.board[move] is not None:
                print('That move is not possible. Space already taken. Please choose another.')
                continue
            self.board[move] = self.turn
            break
    
    def check_winner(self):
        winning_combos = [
            ['a1', 'b1', 'c1']
            ['a2', 'b2', 'c2']
            ['a3', 'b3', 'c3']
            ['a1', 'a2', 'a3']
            ['b1', 'b2', 'b3']
            ['c1', 'c2', 'c3']
            ['a1', 'b2', 'c3']
            ['a3', 'b2', 'c1']
        ]
        for combo in winning_combos:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] !=None: 
                self.winner = self.turn
                return True
            
        return False

    def check_tie(self):
        

    
game_instance = Game()

#print(game_instance.play_game(), game_instance.print_board(), game_instance.print_message())

game_instance.play_game()
game_instance.get_move()
game_instance.print_board()



    
