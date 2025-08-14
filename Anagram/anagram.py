def find_anagrams(word, candidates):
    """Find anagrams of a word in a list of candidates.
    Args:
        word (str): The word to find anagrams for.
        candidates (list): A list of candidate words.
    Returns:
        list: A list of anagrams found in the candidates.
    """
    word_lower = word.lower()
    anagrams = []
    for words in candidates:
        if word_lower == words.lower():
            continue
        if sorted(words.lower()) == sorted(word_lower):
            anagrams.append(words)
    return anagrams
