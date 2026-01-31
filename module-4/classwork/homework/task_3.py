N = 6
knight_moves = [
    (2,1), (1,2), (-1,2), (-2,1),
    (-2,-1), (-1,-2), (1,-2), (2,-1)
]

def print_board(board):
    line = "-" * (4 * N + 1)
    print(line)
    for row in board:
        row_str = "|".join(f" {cell:2} " for cell in row)
        print(f"|{row_str}|")
        print(line)

def is_valid(x, y, board):
    if x < 0 or x >= N:
        return False
    
    if y < 0 or y >= N:
        return False
    
    if board[x][y] != -1:
        return False
    
    return True

def solve(x, y, move_num, board):
    if move_num == N * N:
        return True
    
    for dx, dy in knight_moves:
        nx, ny = x + dx, y + dy

        if is_valid(nx, ny, board):
            board[nx][ny] = move_num + 1

            if solve(nx, ny, move_num + 1, board):
                return True
            
            board[nx][ny] = -1

    return False

def main():
    board = [[-1 for _ in range(N)] for _ in range(N)]

    x_input = input(f"Введите X (0-{N-1}): ")
    y_input = input(f"Введите Y (0-{N-1}): ")

    if not (x_input.isdigit() and y_input.isdigit()):
        print("Введите положительный целые числа")
        return
    
    start_x = int(x_input)
    start_y = int(y_input)

    board[start_x][start_y] = 1
    print(f"Начало: ({start_x}, {start_y})")
    print_board(board)

    if solve(start_x, start_y, 1, board):
        print("Маршрут найден")
        print_board(board)
    else:
        print("Маршрут не найден. Попробуйте другую начальную позицию")
        print("Текущее состояние доски:")
        print_board(board)

main()





