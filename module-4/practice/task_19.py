import random

board = [1, 2, 3, 4, 5, 6, 7, 8, 0]

def print_board():
    print(f"{board[0]:2} | {board[1]:2} | {board[2]:2}")
    print("---+----+---")
    print(f"{board[3]:2} | {board[4]:2} | {board[5]:2}")
    print("---+----+---")
    print(f"{board[6]:2} | {board[7]:2} | {board[8]:2}")

def find_empty():
    return board.index(0)

def is_valid_move(selected):
    empty = find_empty()
    neighbors = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4, 6],
        4: [1, 3, 5, 7],
        5: [2, 4, 8],
        6: [3, 7],
        7: [6, 4, 8],
        8: [5, 7]
    }
    return selected in neighbors[empty]

def make_move(selected):
    if is_valid_move(selected):
        empty = find_empty()
        board[empty], board[selected] = board[selected], board[empty]
        return True
    return False

def is_solved():
    return board == [1, 2, 3, 4, 5, 6, 7, 8, 0]

def shuffle_board():
    for _ in range(100):
        empty = find_empty()
        neighbors = {
            0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
            3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
            6: [3, 7], 7: [6, 4, 8], 8: [5, 7]
        }
        move = random.choice(neighbors[empty])
        board[empty], board[move] = board[move], board[empty]

def main():
    print("Пятнашки 8×8")
    print("Введите номер ячейки (1..8), чтобы переместить её к пустой (0).")
    print("Цель: собрать по порядку от 1 до 8, пустая — внизу справа.")
    shuffle_board()

    while True:
        print_board()
        if is_solved():
            print("Поздравляю! Вы собрали пазл!")
            break

        choice_str = input("Ваш ход (номер ячейки 1-8): ")

        if not choice_str.isdigit():
            print("Введите число от 1 до 8")
            continue

        choice = int(choice_str)
        if choice < 1 or choice > 8:
            print("Число должно быть от 1 до 8")

        idx = choice - 1
        if board[idx] == 0:
            print("Это пустая ячейка")
            continue

        if not make_move(idx):
            print("Нельзя переместить эту ячейку")
            continue

main()
