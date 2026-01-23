def func_3(length, direction, symbol):
    if direction == "h":
        print(symbol * length)
    elif direction == "v":
        for _ in range(length):
            print(symbol)

func_3(length=6, direction="h", symbol="-")



        