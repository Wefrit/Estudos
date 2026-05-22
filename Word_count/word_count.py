import re
from collections import Counter

def count_words(sentence):
    phrase = re.sub(r"[^\w\s']|_", " ", sentence).lower()
    words = phrase.split()
    cleaned_words = [w.strip("'") for w in words if w.strip("'")]
    return Counter(cleaned_words)
