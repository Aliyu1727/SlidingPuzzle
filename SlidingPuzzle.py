import random
import copy
import os
import time

class SlidingPuzzle:
    def __init__(self, size=3):
        self.size = size
        self.goal_state = [[(i * size + j + 1) % (size * size) for j in range(size)] for i in range(size)]
        self.board = copy.deepcopy(self.goal_state)
        self.move_count = 0
        self.start_time = time.time()
        self.shuffle_board()

    def shuffle_board(self):
        moves = ['w', 'a', 's', 'd']
        for _ in range(1000):
            self.move(random.choice(moves), count_move=False)

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Sliding Puzzle Game")
        for row in self.board:
            print(" ".join([f"{num:2}" if num != 0 else "  " for num in row]))
        print(f"\nMoves: {self.move_count}")
        elapsed_time = int(time.time() - self.start_time)
        print(f"Time: {elapsed_time} seconds")

    def find_zero(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return i, j

    def move(self, direction, count_move=True):
        i, j = self.find_zero()
        moved = False
        if direction == 'w' and i < self.size - 1:
            self.board[i][j], self.board[i + 1][j] = self.board[i + 1][j], self.board[i][j]
            moved = True
        elif direction == 's' and i > 0:
            self.board[i][j], self.board[i - 1][j] = self.board[i - 1][j], self.board[i][j]
            moved = True
        elif direction == 'a' and j < self.size - 1:
            self.board[i][j], self.board[i][j + 1] = self.board[i][j + 1], self.board[i][j]
            moved = True
        elif direction == 'd' and j > 0:
            self.board[i][j], self.board[i][j - 1] = self.board[i][j - 1], self.board[i][j]
            moved = True
        
        if moved and count_move:
            self.move_count += 1

    def is_solved(self):
        return self.board == self.goal_state

def play_game():
    puzzle = SlidingPuzzle(size=3)
    
    while True:
        puzzle.display()
        if puzzle.is_solved():
            elapsed_time = int(time.time() - puzzle.start_time)
            print("Congratulations! You solved the puzzle!")
            print(f"Total moves: {puzzle.move_count}")
            print(f"Total time: {elapsed_time} seconds")
            break
        
        move = input("Move (w: up, s: down, a: left, d: right): ").lower()
        if move in ['w', 'a', 's', 'd']:
            puzzle.move(move)
        else:
            print("Invalid move. Use w/a/s/d.")


def main():
    while True:
        play_game()
        replay = input("Do you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
