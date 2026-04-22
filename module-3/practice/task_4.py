text = "Hello World"
replacements = {"e": 1, "l": 1, "o": 1, "r": 1}
result = ""

for char in text:
    result += str(replacements.get(char, char))

print(result)



