def encode(plain_text):
    alphabet = [
        "a","b","c","d","e",
        "f","g","h","i","j",
        "k","l","m","n","o",
        "p","q","r","s","t",
        "u","v","w","x","y","z"
                ]

    tebahpla = [
        "z","y","x","w","v",
        "u","t","s","r","q",
        "p","o","n","m","l",
        "k","j","i","h","g",
        "f","e","d","c","b","a"
                ]
    new_txt = "".join(plain_text.lower().split())
    decoded_text = ""
    for c in new_txt:
        if c in alphabet:
            decoded_text += (tebahpla[alphabet.index(c)])
        else:
            decoded_text += c
    return decoded_text        


print(encode("OM G"))