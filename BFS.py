import tkinter as tk
from tkinter import messagebox
import random
from collections import deque
class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = [""] * 9
        self.current_player = "X"
        self.buttons = [tk.Button(master, text="", font='Arial 20', width=5, height=2,
                                   command=lambda i=i: self.player_move(i)) for i in range(9)]
        for i, button in enumerate(self.buttons):
            button.grid(row=i // 3, column=i % 3)

    def player_move(self, index):
        if self.board[index] == "" and self.current_player == "X":
            self.board[index] = "X"
            self.buttons[index].config(text="X")
            if self.check_winner("X"):
                messagebox.showinfo("Game Over", "You win!")
                self.reset_game()
            else:
                self.current_player = "O"
                self.computer_move()

    def computer_move(self):
        # Placeholder for your search algorithm
        index = self.get_computer_move()
        if index is not None:
            self.board[index] = "O"
            self.buttons[index].config(text="O")
            if self.check_winner("O"):
                messagebox.showinfo("Game Over", "Computer wins!")
                self.reset_game()
            else:
                self.current_player = "X"

    #<---------------------------BFS------------------------------>

    def get_computer_move(self):
        # created a queue
        q = deque() 
        v = set()  # Use a set for visited states
        available_moves = [i for i in range(9) if self.board[i] == ""]

        # Enqueue initial states for available moves
        for move in available_moves:
            new_board = self.board[:]
            new_board[move] = "O"  # Simulate placing "O"
            q.append((new_board, move))

        while q:
            current_state, move = q.popleft()

            # Check if this move wins the game for "O"
            if self.check_winner("O"):
                return move  # This move wins the game

            # Check if this state leads to a loss for "X"
            if self.check_winner("X"):
                continue  # Skip this state

            # Explore further moves
            for next_move in available_moves:
                if current_state[next_move] == "":
                    new_board = current_state[:]
                    new_board[next_move] = "X"  # Simulate placing "X"
                    if tuple(new_board) not in v:  # Check if state is visited
                        v.add(tuple(new_board))
                        q.append((new_board, next_move))

        # If no winning move found, return a random available move
        return random.choice(available_moves)
        
        

    def check_winner(self, player):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), #winning rows
                                (0, 3, 6), (1, 4, 7), (2, 5, 8), #winning columns
                                (0, 4, 8), (2, 4, 6)] #winning diagonals
        return any(all(self.board[i] == player for i in combo) for combo in winning_combinations)

    def reset_game(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

