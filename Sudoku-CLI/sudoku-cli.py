import random


def print_grid(grid):
    """Prints the Sudoku grid in a formatted manner."""
    def print_separator():
        print("-" * 21)
    
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print_separator()
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(grid[i][j] if grid[i][j] != 0 else '.', end=" ")
        print()


def is_valid(grid, row, col, num):
    """Check if num can be placed at grid[row][col]"""
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False
    
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True


def find_empty_cell(grid):
    """Finds the next empty cell using a heuristic to prioritize more constrained cells."""
    empty_cells = []
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                possibilities = sum(is_valid(grid, i, j, num) for num in range(1, 10))
                empty_cells.append((possibilities, i, j))
    return min(empty_cells, default=(None, -1, -1))[1:] if empty_cells else (-1, -1)


def solve(grid):
    """Solves the Sudoku puzzle using backtracking with a heuristic-based approach."""
    row, col = find_empty_cell(grid)
    if row == -1:
        return True  # Puzzle solved

    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve(grid):
                return True
            grid[row][col] = 0
    return False


def generate_sudoku(initial_numbers=11):
    """Generates a random Sudoku puzzle with a specified number of initially placed numbers."""
    grid = [[0 for _ in range(9)] for _ in range(9)]
    available_positions = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(available_positions)
    
    count = 0
    while count < initial_numbers and available_positions:
        row, col = available_positions.pop()
        num = random.randint(1, 9)
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            count += 1
    
    return grid


def play():
    """Main function to play the Sudoku game."""
    grid = generate_sudoku()
    while True:
        print_grid(grid)
        move = input("Enter row, col, number (or 'solve' to auto-solve, 'quit' to exit): ")
        if move.lower() == 'quit':
            break
        if move.lower() == 'solve':
            solve(grid)
            print("Solved Sudoku:")
            print_grid(grid)
            break
        try:
            row, col, num = map(int, move.split())
            if 1 <= row <= 9 and 1 <= col <= 9 and 1 <= num <= 9:
                if grid[row-1][col-1] == 0 and is_valid(grid, row-1, col-1, num):
                    grid[row-1][col-1] = num
                else:
                    print("Invalid move!")
            else:
                print("Enter numbers between 1-9!")
        except ValueError:
            print("Invalid input format!")


if __name__ == "__main__":
    play()
