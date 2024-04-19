def check_word(word):
    if len(word) >= 10:
        return "palavrao"
    else:
        return "palavrinha"

try:
    while True:
        word = input().strip()
        print(check_word(word))
except EOFError:
    pass