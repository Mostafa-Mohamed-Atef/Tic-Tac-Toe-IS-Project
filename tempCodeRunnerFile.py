    def check_winner_for_board(self, player, board):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        return any(all(board[i] == player for i in combo) for combo in winning_combinations)
