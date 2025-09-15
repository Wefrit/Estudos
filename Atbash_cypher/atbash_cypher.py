import string

def encode(plain_text):
    alphabet = string.ascii_lowercase
    reversed_alphabet = alphabet[::-1]

    result = []
    for c in plain_text.lower():
        if c.isalpha():
            result.append(reversed_alphabet[alphabet.index(c)])
        elif c.isdigit():
            result.append(c)

    grouped = [''.join(result[i:i+5]) for i in range(0, len(result), 5)]
    return ' '.join(grouped)


def decode(cipher_text):
    alphabet = string.ascii_lowercase
    reversed_alphabet = alphabet[::-1]

    cipher_text = ''.join(c for c in cipher_text.lower() if c.isalnum())

    result = []
    for c in cipher_text:
        if c.isalpha():
            result.append(alphabet[reversed_alphabet.index(c)])
        else:
            result.append(c)
    return ''.join(result)
