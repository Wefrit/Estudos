import re
from collections import Counter
def count_words(sentence):
    phrase = re.sub(r"[^a-zA-Z0-9\s]","", sentence)
    words = phrase.split()
    return Counter(words)

print(count_words("Teste inicial de algumas palavras e um numero que vai ser 254 preciso de palavras repetidas"))

