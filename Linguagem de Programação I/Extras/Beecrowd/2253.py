import re

def validate_password(password):
    if not 6 <= len(password) <= 32:
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if re.search(r'\W', password):
        return False
    return True

try:
    while True:
        password = input().strip()
        if validate_password(password):
            print("Senha valida.")
        else:
            print("Senha invalida.")
except EOFError:
    pass