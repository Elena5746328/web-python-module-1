text = "Сложнее всего начать действовать, все остальное зависит только от упорства."
def count_sentences(text):
    count = 0
    for char in text:
        if char == "." or char == "!" or char == "?":
            count += 1
    return count

print(f"Предложений: {count_sentences(text)}")


