def func_7(number):
    x = str(number)
    if len(x) != 6:
        return False
    return sum(map(int, x[:3])) == sum(map(int, x[3:]))

print(func_7("123420"))

    
