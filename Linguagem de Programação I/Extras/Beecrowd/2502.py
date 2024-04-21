def decipher(cipher, ciphered_text):
    deciphered_text = ""
    for char in ciphered_text:
        if char.upper() in cipher:
            if char.isupper():
                deciphered_text += cipher[char.upper()].upper()
            else:
                deciphered_text += cipher[char.upper()].lower()
        else:
            deciphered_text += char
    return deciphered_text

def process_input():
    while True:
        try:
            C, N = map(int, input().split())
            cipher_key_1 = input()
            cipher_key_2 = input()
            cipher = {cipher_key_1[i]: cipher_key_2[i] for i in range(C)}
            cipher.update({cipher_key_2[i]: cipher_key_1[i] for i in range(C)})
            for _ in range(N):
                ciphered_text = input()
                print(decipher(cipher, ciphered_text))
            print()
        except EOFError:
            break

process_input()