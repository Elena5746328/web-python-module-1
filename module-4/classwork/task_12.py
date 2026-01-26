def sum(a, b):
    if a == b:
        return a
    
    return a + sum(a + 1, b)

print(sum(3, 5))