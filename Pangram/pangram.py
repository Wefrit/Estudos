def is_pangram(sentence):
    """Determine if a sentence is a pangram.

    A pangram (Greek: παν γράμμα, pan gramma, "every letter") is a sentence using every letter of the alphabet at least once.
    The best known English pangram is:
        "The quick brown fox jumps over the lazy dog."
    Args:
        sentence (str): The sentence to evaluate.
    Returns:
        bool: True if the sentence is a pangram, False otherwise.   
    """
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    sentence_set = set(sentence.lower())
    return alphabet.issubset(sentence_set)
