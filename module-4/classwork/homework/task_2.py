import random

def generate_secret():
    digits = list(range(10))
    number = []

    first = random.choice(digits[1:])
    number.append(first)
    digits.remove(first)

    for _ in range(3):
        chosen = random.choice(digits)
        number.append(chosen)
        digits.remove(chosen)

    return "".join(map(str, number))

def get_guess():
    while True:
        s = input("Введите четырёхзначное число: ").strip()
        if len(set(s)) != 4:
            print("Ошибка: все цифры должны быть разными")
            continue
        return s
    
def count_bulls_and_cows(secret, guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

def print_status(bulls, cows):
    print(f"Быки: {bulls}, Коровы: {cows}")

def game_loop(secret, attempts):

    guess = get_guess()
    bulls, cows = count_bulls_and_cows(secret, guess)
    print_status(bulls, cows)

    if bulls == 4:
        print(f"Победа! Вы угадали число {secret} за {attempts} попыток")
        return
    else:
        game_loop(secret, attempts + 1)

def play_game():
    secret_number = generate_secret()
    attempts = 1

    print("Добро пожаловать в игру 'Быки и коровы'")
    print("Я загадала 4-значное число с неповторящими цифрами")
    print("Попробуйте угадать его")
    print("После каждой попытки будет высвечиваться следующее:")
    print(" - сколько цифр угадано и стоит на своем месте(быки),")
    print(" - сколько цифр есть в числе, но не на своем месте(коровы)")

    game_loop(secret_number, attempts)

play_game()