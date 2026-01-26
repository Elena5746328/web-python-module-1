def star(n):
    if n <= 0:
        return
    print("*", end = " ")
    star(n - 1)

star(5)
    
